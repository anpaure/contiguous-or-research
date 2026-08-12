# K17 canonical drop-12 consumer rebase and target-20 Hall contract

Date: 2026-08-03

Status: authoritative parent rebase, exact target-20 Hall theorem, and
proof-safe consumer contract.  The H100 producer root is authoritative.
The historical all-27 table remains a valid ancestor witness, but none of
its prospective catalogue IDs or compiled incidences is active here.

## 1. Authoritative recursive node

The unique prospective consumer node is

\[
\Pi_{12}=
(C_{12},S_{10},T_{12},\mathcal P_{7213},
 \Omega_{23},R_{26},\mathcal K_{12}),
\tag{1.1}
\]

where

\[
C_{12}=
\texttt{e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb}
\tag{1.2}
\]

is the compressed normal carrier and

\[
T_{12}=
\texttt{fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c}
\tag{1.3}
\]

is its fixed ten-mode final overlay.  The selected 26-action root ledger has
SHA

\[
\texttt{8c6c662344728fb6ce7a3dbb58c2946aec0313abc7385ba3a10512d33523d21c}.
\tag{1.4}
\]

The remaining node components bind the 7,213 protected rows, the exact
23-row two-phase occurrence union, the fixed-ten overlay policy, owner/root
presentation, and the catalogue/compiler semantics.  A table SHA alone is
not a complete node identity.

The authoritative producer root is

\[
\texttt{/home/amodo/or15/work/
k17\_drop12\_canonical\_consumer\_catalogue\_20260803}.
\tag{1.5}
\]

Its 50-payload frozen manifest has SHA

\[
\texttt{b54013519c97e24ee35de8db0033afff9b407f7e6daf47cfdff89ddbe7420d93}.
\tag{1.6}
\]

The human handoff and machine manifest have respective SHAs

\[
\texttt{360b294e6d6655e2f50ceb28fc9c1aafd9467a182fcfdc9c3a37c4df52d417c4},
\tag{1.7}
\]

\[
\texttt{95e6f5b38cc8cd942feeddbaaa8645c75d5acf004c18598469f89531411d50be}.
\tag{1.8}
\]

The exact complete 6/9/4 supplier projection of \(T_{12}\) has

\[
|E|=74935,\qquad |H|=16898,\qquad
\nu=16877,\qquad \delta=21,
\tag{1.9}
\]

with 19 zero heads and a maximum Hall shore of 23 heads and two suppliers.

## 2. Scoped two-payload transfer repair

A separate local mirror was observed while still hydrating: the full
common-state ledger was absent and the transported phase-1 price ledger was
temporarily mismatched.  Neither producer artifact was modified.

Only those two payloads were fetched from the H100 authority into the unique
audit directory

\[
\texttt{scratch/
audit\_k17\_drop12\_consumer\_payload\_resync\_20260803\_019fc2ce}.
\tag{2.1}
\]

The exact audit-only destinations and authoritative hashes are:

| H100 producer-relative payload | audit-only destination | SHA-256 |
|---|---|---|
| out/exact_state_common.coalesced.tsv | exact_state_common.coalesced.tsv | 713fa2ebf7f9e01071ea6f22e75f705a88e88af487cd5bed42375a8dbcff0ca8 |
| out/transported_p1.price.tsv | transported_p1.price.tsv | 2f6f4c0a2afe81edda313d83855f6d678bce282997b31877c7a4fe17728217a1 |

The fresh files contain respectively 5,127 lines / 348,152 bytes and
114,595 lines / 5,788,911 bytes.  Both hashes equal their entries in the
SHA-\(\texttt{b5401351}\) producer manifest.  The audit-only resync manifest
has SHA

\[
\texttt{758b0c3054a0147c989e65a8f96a00dfd8b2f46a424563884dee481d3fb86c98}.
\tag{2.2}
\]

Therefore the observed defect is transfer/hydration-only.  It changes no
producer payload, catalogue census, parent state, phase semantics, supplier
rank, or mathematical conclusion.

## 3. Parent-local catalogue semantics

Let \(E_{12}\) be the structural catalogue generated from \(C_{12}\).
The authoritative counts are:

\[
\begin{array}{c|r}
\text{catalogue layer}&\text{count}\\\hline
\text{static structural containment modes}&114594\\
\text{native phase-0 marginal-positive modes}&15659\\
\text{transported phase-1 marginal-positive modes}&17779\\
\text{common declared-state modes}&5126\\
\text{common selected-witness pin-safe modes}&3494\\
\text{strict selected-tuple-equal modes}&3037\\
\text{strict selected-tuple-equal and pin-safe modes}&2813.
\end{array}
\tag{3.1}
\]

The structural ledger has SHA

\[
\texttt{790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434}.
\tag{3.2}
\]

Its 114,594 ordinals are the only prospective mode IDs.  They must be
namespaced by \((\operatorname{digest}(\Pi_{12}),\text{catalogue SHA},
\text{local ordinal},\text{payload SHA})\).

The layers in (3.1) have different meanings:

1. structural membership proves only endpoint containment on \(C_{12}\);
2. phase-positive membership is an exact one-mode marginal certificate in
   that phase;
3. common membership proves that the two phase ledgers share at least one
   declared \((q,\alpha,\beta)\) key, while physical predecessor/successor
   rows may differ;
4. pin-safe membership is a sufficient filter for the one deterministically
   selected coalesced witness against the fixed 23-row occurrence union; and
5. strict tuple equality is a cheaper sufficient subface over those selected
   witnesses, not an exhaustive search over alternative physical witnesses.

None of these counts proves that two or more modes pack simultaneously.
Endpoint rows, phase-specific witness rows, coalesced cross-phase histories,
the 23 fixed occurrence rows, the protected ledger, and the fixed-ten
overlay resources must be capacity-checked jointly.

The ten incumbents have one authenticated literal endpoint/payload rebind,
SHA

\[
\texttt{b34b14be304a0369b420126ac1c90c2570e118f33dd4ed3aad69c7894a34f8f2}.
\tag{3.3}
\]

This rebind authenticates the baseline overlay; it does not make an ancestor
ordinal prospective.  If an incumbent is fixed, a new mode sharing its
endpoint is unavailable.  If replacement is allowed, that release and every
affected occurrence/state prerequisite must be explicit in the lifted state.

### Lemma 3.1 (safe reuse of a marginal witness)

A stored marginal column
\((e,k,\omega_0,\omega_1)\) remains a valid two-phase socket after a joint
materialization \(T_X\) if, in each phase, \(T_X\) agrees with the column's
single-edge witness table on:

- the candidate MR bottom, root, and owner;
- every predecessor/successor row's long family, root, owner, and selected
  flag; and
- all endpoint, capacity, and shared-history conditions used by the literal
  witness.

#### Proof

The incoming, outgoing, and common-five-cell predicates read exactly those
local data.  Equality on all read data preserves their truth.  Joint capacity
and history feasibility is stated separately because it is not a unary
property of a stored column. \(\square\)

Pin-disjointness is a convenient sufficient screen for part of this lemma;
it is not by itself the lemma's full hypothesis.  Supplier rank is global and
does not follow from it.

## 4. Exact target-20 Hall separator

Let \(Q_{12}\) be the authenticated 23-head maximum shore of \(T_{12}\).
Its current distinct supplier rows are

\[
N_{T_{12}}(Q_{12})=\{12973,14851\}.
\tag{4.1}
\]

For a complete simultaneously materialized candidate \(\theta\), define

\[
A_h(\theta)=1
\quad\Longleftrightarrow\quad
h\text{ retains its exact frozen }Q_{12}\text{ head state},
\tag{4.2}
\]

\[
D_h(\theta)=1-A_h(\theta),
\tag{4.3}
\]

and, for every physical supplier row \(u\in\{0,\ldots,24309\}\),

\[
N_u^{Q_{12}}(\theta)=
\bigvee_{\substack{h\in Q_{12}\\u\ne h}}
\left[
A_h(\theta)\wedge
\operatorname{Compatible}_{6/9/4}
(\operatorname{State}_{\theta}(u),\operatorname{Req}(h))
\right].
\tag{4.4}
\]

Each physical supplier row contributes at most one OR credit, regardless of
how many heads or flag pairs it supports.  The guard \(u\ne h\) is the exact
self-edge exclusion of the authenticated supplier graph.

### Theorem 4.1 (canonical target-20 cut)

Every child of supplier deficiency at most 20 satisfies

\[
\boxed{
\sum_{h\in Q_{12}}D_h(\theta)
+
\sum_{u=0}^{24309}N_u^{Q_{12}}(\theta)
\ge |Q_{12}|-20=3.}
\tag{4.5}
\]

#### Proof

The first sum counts inactive frozen head states, each represented by its
private dummy supplier.  The second is exactly the cardinality of the
distinct compatible physical-supplier neighborhood of the active states.
Their sum is the completed neighborhood cardinality.  Rearranging Hall's
deficiency inequality gives (4.5). \(\square\)

At the canonical parent the first sum is zero and the second is two, so the
left side is \(2<3\).  If \(d_Q\) old head states are deactivated,
\(\ell\) of the two current neighbors are lost, and \(g\) genuinely new
distinct neighbors are exposed, (4.5) is exactly

\[
\boxed{d_Q+g-\ell\ge1.}
\tag{4.6}
\]

Thus the next target requires one **net** Hall credit, not one selected mode
and not one marginal-positive record.  The two current neighbor rows are
calibration values, not a closed future-neighbor menu; a valid master must
implement all 24,310 row-state ORs in (4.4), or evaluate them lazily after
materialization.

The separately frozen target-20 separator package has a 14-file manifest,
all locally verified, with SHA

\[
\texttt{9fe0db28f18ee763cb82a204ffec6ef21791a322c2e6cf46d9cd4d0e3fe7e80d}.
\tag{4.7}
\]

Its semantic bundle digest is
\(\texttt{df8df82467803172c08fa8557521064ba2c6bbd2279ef949467b742ea13f6b3a}\).
Equation (4.5) is necessary, not sufficient; another shore may become
controlling after it is satisfied.

### Theorem 4.2 (adaptive-recourse all-shore contraction)

Let \(\theta_0=\Pi_{12}\), with deficiency 21, and let \(\theta'\) be one
fully materialized child.  Work over an authenticated common semantic head
universe \(\mathcal H\), assumed finite, and give every inactive head its own
private dummy supplier.  For every semantic shore \(Q\), define

\[
g_\theta(Q)=|N_{\widehat G_\theta}(Q)|,
\qquad
\kappa_\theta(Q)=|Q|-g_\theta(Q).
\tag{4.8}
\]

Then exact contraction to target 20 is equivalent to the complete erosion
system

\[
\boxed{
\delta(\theta')\le20
\quad\Longleftrightarrow\quad
g_{\theta'}(Q)-g_{\theta_0}(Q)
\ge\kappa_{\theta_0}(Q)-20
\quad(Q\subseteq\mathcal H).}
\tag{4.9}
\]

#### Proof

For every \(Q\),

\[
\kappa_{\theta'}(Q)
=\kappa_{\theta_0}(Q)
-\left(g_{\theta'}(Q)-g_{\theta_0}(Q)\right).
\tag{4.10}
\]

Thus (4.9) is equivalent shore by shore to
\(\kappa_{\theta'}(Q)\le20\).  Taking the maximum over \(Q\) proves the
claim. \(\square\)

Since \(g_{\theta_0}(Q)+\kappa_{\theta_0}(Q)=|Q|\), each erosion inequality
is algebraically the ordinary child Hall row

\[
g_{\theta'}(Q)\ge |Q|-20.
\tag{4.11}
\]

The erosion form records what representation recourse is allowed to lose:
every parent-deficiency-21 shore must gain at least one, every
parent-deficiency-20 shore may lose nothing, and a shore with parent
deficiency \(20-t\) may lose at most \(t\).

For \(Q_{12}\), \(\kappa_{\theta_0}(Q_{12})=23-2=21\), so (4.9) reduces
exactly to (4.5)--(4.6).  Consequently the incumbent 23/2 row is a valid
first pruning inequality only.  Passing it does not certify contraction:
recourse may improve \(Q_{12}\) while eroding another tight or near-tight
shore.

The quantifier is one common child:

\[
\exists(z,\xi)\ \forall Q\subseteq\mathcal H,
\tag{4.12}
\]

not a different recourse completion for each shore.  For a robust
action-level claim, the completion set must be nonempty before any
universal-over-recourse statement is used.

### Corollary 4.3 (child-local augmentation certificate)

Exact target 20 is also equivalent to the existence, in the same fully
recomputed completed child graph \(\widehat G_{\theta'}\), of:

1. a matching \(M_0\) of size 16,877; and
2. an \(M_0\)-augmenting path.

The augmentation gives a matching of size 16,878.  Conversely, deleting one
edge from any 16,878-edge child matching gives such an \(M_0\), with the
deleted edge as a length-one augmenting path.  The matching \(M_0\) is not
maximum in the child.  Neither the parent matching nor an old DM augmenting
path transports through representation/common-basis recourse.

### Theorem 4.4 (exact common-bank one-mode filter)

Let \(\mathcal C_{\rm pin}\) be the 3,494 pin-disjoint exact-common records,
and let \(\mathcal C_{3483}\) be the literal one-mode pool after removing the
11 incumbent-endpoint conflicts.  For each
\(e\in\mathcal C_{\rm pin}\), the exact downstream ledger records both endpoints and
the selected native-phase-0/transported-phase-1 predecessor/successor rows.
Every such full local footprint avoids all 23 rows of \(Q_{12}\) and all 19
current zero heads.  Hence a literal one-mode overlay with
\(e\in\mathcal C_{3483}\) has

\[
d_Q(e)=\sum_{h\in Q_{12}}D_h(T_e)=0.                       \tag{4.13}
\]

Put \(S_0=\{12973,14851\}\), and define the genuinely new and lost physical
supplier identities

\[
G_e=\{u\notin S_0:N_u^{Q_{12}}(T_e)=1\},\qquad
L_e=\{u\in S_0:N_u^{Q_{12}}(T_e)=0\}.                     \tag{4.14}
\]

Then (4.6) becomes

\[
\boxed{|G_e|\ge1+|L_e|.}                                  \tag{4.15}
\]

The 23/2 shore is the disjoint union of 19 isolated zero heads and two
incidence paths,

```text
13148 -- 12973 -- 12948
15103 -- 14851 -- 1490,
```

where each middle vertex is a physical supplier identity.  Every ordinary
record would therefore have to create a third distinct supplier identity.
Edge 52847 is the unique exception touching the current neighbor set: its LR
endpoint is row 14851, and its exact one-mode replay destroys both incidences
carried by that row.  Thus the Boolean one-mode filter is

\[
\boxed{
\sum_{u\notin\{12973,14851\}}N_u^{Q_{12}}(T_e)
\ge1+\mathbf1[e=52847].}                                  \tag{4.16}
\]

Exact endpoint-incidence replay proves more: none of the 3,483
incumbent-disjoint literal common modes exposes any new shore supplier.
Ordinary modes have credit zero.  Edge 52847 has \(G_e=0\), \(L_e=1\), and
credit minus one.  It is an exact singleton Hall rejection on this literal
face.  A noncommon supplier-source partner may still provide the missing
identities in a simultaneous pair.

#### Proof

Equation (4.13) follows from literal row preservation.  The current
neighborhood contributes \(2-|L_e|\) identities and every identity outside
\(S_0\) contributes once through its exact OR bit, so

\[
\Gamma_{Q_{12}}(T_e)=2-|L_e|+|G_e|.
\]

Substitution in (4.5) proves (4.15).  The exact exceptional-row census and
the two-row materialization rule give (4.16) and the final cardinality
claim. \(\square\)

Fresh structural edge 193 is the complementary calibration.  Its donor is
shore head 12948, its exact replay has one retired frozen head, both current
neighbor identities, and matching \(16878/16898\).  It pays (4.5) as
\(1+2=3\), which explains its supplier positivity.  Both canonical phase
ledgers give `exists=0`, so it has no canonical native/transported common
state and is not an occurrence-valid member of \(\mathcal C_{\rm pin}\).

### Corollary 4.5 (singleton closure does not factor through pairs)

The current structural screen has 515 parent-shore survivors and 468 exact
rank-16,878 one-mode children.  For every one of those 468, the exact
candidate-local phase menus, with the newly materialized LLR host admitted
as a long witness, satisfy

\[
K_e^0\cap K_e^1=\varnothing.                               \tag{4.17}
\]

Equivalently, `raw_common_state=0` for every supplier-improving singleton.
Occurrence requires one declared key supported in both phases, so no choice
of alternative predecessor/successor rows within a key can repair (4.17).
Thus none of the 468 supplier-improving literal one-mode children is
occurrence-common on this canonical face, including with new-host
self-support.

For a pair this conclusion is nonfactorizing.  The partner changes a second
long row state and can create a common key for \(e\), while \(e\)'s new host
can create a key for the partner.  Let \(R_{468}\) be the
supplier-improving source set.  The
exact join is

\[
\mathcal C_{3483}\cap R_{468}=\varnothing.                 \tag{4.18}
\]

Therefore restricting both pair coordinates to
\(\mathcal C_{3483}\) excludes every known supplier-improving source and is
not a complete pair search.  Moreover, the exact resource-disjoint census of
that face is

\[
\begin{array}{c|r}
\text{Hall credit}&\text{pairs}\\\hline
0&5{,}219{,}031\\
-1&2{,}287\\
>0&0
\end{array}                                                 \tag{4.19}
\]

for a total of 5,221,318 pairs.  The minus-one rows are the compatible pairs
containing edge 52847.  No common/common pair changes a shore head or creates
a new shore supplier, so every row of (4.19) violates (4.5).  The
common/common face is exactly dead and may be frozen.

The resource screen leaves every source with 3,477--3,483 common helpers
(2,802--2,807 strict two-row helpers), totaling 1,629,622 ordered seeds.
This proves only the absence of preliminary row-capacity scarcity.  It does
not prove occurrence rescue: both donor long states must be removed, both new
LLR hosts installed, and both phase state-key menus recomputed before joint
ticket capacity and flag consistency are tested.

A complete live pair lane must instead contain at least one coordinate in
\(R_{468}\), enumerate a second structural mode/changed long state capable of
mutual occurrence support, and check the two phase menus and capacities on
the simultaneously materialized child.

## 5. Proof-safe def21-to-def20 consumer protocol

A proposal is a complete lifted state, not a list of ordinals:

\[
\theta=(Z,k,\omega_0,\omega_1,\rho,\pi),
\tag{5.1}
\]

where \(Z\) is the mode set, \(k\) its common declared states,
\(\omega_0,\omega_1\) are literal phase witnesses, \(\rho\) is the joint
root/common-basis completion, and \(\pi\) declares which incumbent modes and
pins remain fixed or are released.

For a two-mode target-20 search, \(Z\) must not be restricted to two members
of the 3,483 individually-common pool.  At least one coordinate must be drawn
from the 468 exact supplier-source set, and the partner must be enumerated by
its ability to create a changed long state that can support a common key on
the joint child (with the converse dependency allowed).  The 3,483 records
remain an exact helper/control pool, while their common/common Cartesian face
is Hall-dead by (4.19) and should be frozen rather than searched.

A proof-safe candidate must:

1. use only \(E_{12}\) ordinals and payloads under (3.2);
2. enforce joint endpoint and witness-row capacities across every selected
   mode, both phases, the protected ledger, \(\Omega_{23}\), and the declared
   fixed portion of \(S_{10}\);
3. impose one shared declared state per supported short role while retaining
   phase-specific literal predecessor/successor rows;
4. constrain the structural/root/common-basis solve by every protected and
   frozen obligation, then run one simultaneous materialization on
   \(C_{12}\), rather than composing unary witnesses;
5. reverify after materialization every protected row, fixed occurrence,
   retained incumbent, and owner/root invariant;
6. emit one canonical final table \(T(\theta)\);
7. rebuild the complete supplier graph from \(T(\theta)\); and
8. compute a fresh maximum supplier matching and residual Hall shore.

The exact target-20 acceptance condition in the fixed
\(|\mathcal H|=16898\) completed semantic graph is

\[
\boxed{\nu(\widehat G_{T(\theta)})\ge16878.}
\tag{5.2}
\]

Equivalently, if \(A_\theta\) is the set of active child heads and
\(G_\theta[A_\theta,\mathcal U]\) is the raw supplier graph, the condition is

\[
\nu(G_\theta[A_\theta,\mathcal U])\ge |A_\theta|-20.
\tag{5.3}
\]

The often quoted raw threshold 16,878 is valid only when
\(|A_\theta|=16898\).  Passing (4.5), common-catalogue membership, or
marginal positivity cannot replace (5.2)--(5.3).  Equivalently, the final
proof may exhibit the child-local 16,877-edge completed matching plus
augmenting path of Corollary 4.3, or verify every all-shore row in (4.9).
In practice a complete target-size matching is the smallest direct
certificate.

If (5.2) fails, the fresh maximum shore supplies the next exact
parent/candidate-local Hall row \(g_{\theta'}(Q)\ge|Q|-20\), equivalently
the violated erosion row in (4.9).  It may be projected into a master only
when all head-activity and supplier-incidence circuits are complete over
every represented completion.  Otherwise the safe result is a lifted
no-good for that exact materialization, or an active-set pricing request.
If no authenticated common semantic head map exists, do not transport
shores at all; use only the full child matching certificate.

A negative proof for a one/two-mode subface must enumerate every physical
witness admitted by that subface or retain missing alternatives as
optimistic UNKNOWN recourse.  The deterministic selected-witness ledgers
alone cannot prove such an UNSAT.  Corollary 4.5 is stronger only because the
two phase **state-key supports themselves** are disjoint for each singleton;
it is not a first-witness conflict.  That key-support result must be recomputed
after both pair modes are installed and cannot be reused as a unary no-good.

Any accepted child receives a new carrier/final pair and node digest.
Its structural catalogue, phase prices, common-state joins, supplier graph,
and Hall cuts must then be regenerated.  No incidence monotonicity is
assumed across that rebase.

## 6. Stale-ID theorem

The all-27/dd608 catalogue is valid only as historical calibration.  Relative
to the older catalogue, the canonical drop-12 rebase removed 3,417 endpoint
pairs, added 2,925 pairs, and changed the payload of 36 retained pairs.
Enumeration coordinates and phase/state predicates are therefore
parent-dependent.

### Theorem 6.1

No prospective claim on \(\Pi_{12}\) may use a bf5, all-27, or dd608 numeric
mode ID.  A historical mode transports only through an authenticated exact
endpoint-and-payload rebind into the SHA-\(\texttt{790fae94}\) catalogue.

#### Proof

A numeric ancestor ID identifies neither a stable endpoint pair nor a stable
payload after deletions, insertions, and payload changes.  Phase witnesses,
pin overlap, and supplier effects also depend on the new table.  Exact
semantic rebind is therefore necessary. \(\square\)

The dd608 joint witness and its deficiency-22 theorem remain valid ancestor
facts.  Only their use as a prospective consumer namespace is superseded.

## 7. Scope

This rebase is exact for the fixed ten-mode/23-occurrence, selected 26-root
face and the complete 6/9/4 row-pair supplier projection.  It does not prove
address/state circulation, residual long--long chronology, residence, upper
coverage, common-cap compilation, a final compiler/word, total unimodularity,
or global K17 optimality.

The frozen conclusion is

\[
\boxed{
\Pi_{12}\text{ is the sole active consumer node;}
\quad \Gamma_{Q_{12}}\ge3\text{ is pruning only;}
\quad \text{acceptance requires simultaneous materialization and either}
\quad \nu(\widehat G)\ge16878
\quad\text{or}\quad\nu(G[A,\mathcal U])\ge|A|-20.}
\tag{7.1}
\]

Within this node, the 5,221,318 resource-disjoint common/common pairs are an
exact Hall no-go and are frozen.  The remaining target-20 pair lane is
source/helper: it contains at least one of the 468 exact supplier sources and
validates mutual occurrence only after joint materialization.
