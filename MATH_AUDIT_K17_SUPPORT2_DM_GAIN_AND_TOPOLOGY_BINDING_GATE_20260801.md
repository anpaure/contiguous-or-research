# K17 support-two circuits: exact DM gains and the topology-binding gate

Date: 2026-08-01  
Factor: `scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/serial_round2_reverse.candidate.tsv`  
Circuit bank: `scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/serial_round2_reverse.support2_root_perfect_matching.tsv`

## 1. Why merge/preserve/split is not yet defined

The rooted table is an exact static type/lower-palette factor, but it is not a
chronology.  Its exact common-live root/owner incidence graph has maximum
matching

\[
\nu(H)=936<1430,
\]

with Hall shore

\[
|X|=652,\qquad |N(X)|=158,\qquad |X|-|N(X)|=494.
\]

Therefore no common root-owner live-state transversal exists.  In particular,
there is no selected attachment state at every root, no selected successor arc
at every state, and no quotient cycle/path forest whose components a circuit
could canonically merge or split.

This is not a technicality: a maximum root/owner matching selects live
incidences, not mutually consistent transition arcs between those incidences.
Its edges alone do not form a transition forest.

Thus assigning a chronology sign to the 715 circuits from the static factor
would be invented data.  The strongest canonical pre-chronology signs are
maximum-matching gain and Dulmage--Mendelsohn cut/rank gain.

## 2. Canonical DM audit

For every one of the 715 literal support-two circuits, independently apply
that circuit to the authenticated factor, rebuild every literal rooted and
attachment-state transition, and recompute:

1. the packet-support maximum matching;
2. the common-live root/owner maximum matching;
3. new and removed common-live incidences;
4. incidences crossing the baseline Hall shore;
5. graphic rank of the new incidences after contracting the directed-DM SCCs.

The baseline directed DM graph is oriented from left roots to right owners on
unmatched incidences and from right owners to left roots on matched incidences.
It has 2860 SCCs in this instance, so every SCC is a singleton.  The reported
contracted ranks are nonetheless kept in the invariant form needed for later
instances.

## 3. Exact individual signs

The common-live matching gains are

| gain | circuits |
|---:|---:|
| -5 | 5 |
| -4 | 24 |
| -3 | 119 |
| -2 | 197 |
| -1 | 219 |
| 0 | 115 |
| +1 | 34 |
| +2 | 2 |

Hence 36 of the 715 circuits are canonically common-live augmenting.  Because
the original bank is root-perfect, these 36 circuits are already pairwise
root-disjoint.  Their support graph has matching number and DM-contracted
graphic rank 36.  Their newly exposed common-live incidences have
DM-contracted graphic rank 101.

The packet-support gains are much harsher:

| gain | circuits |
|---:|---:|
| -4 | 10 |
| -3 | 152 |
| -2 | 346 |
| -1 | 177 |
| 0 | 30 |

No circuit in this particular root-perfect bank improves packet-support
matching.  Only five circuits improve common-live matching without decreasing
packet-support matching:

| circuit | roots | common gain | packet gain |
|---:|---:|---:|---:|
| 212 | 288,679 | +2 | 0 |
| 327 | 464,819 | +1 | 0 |
| 399 | 583,1186 | +1 | 0 |
| 457 | 689,854 | +1 | 0 |
| 631 | 1041,1189 | +1 | 0 |

These five disjoint circuits compose exactly: applying all five preserves the
packet matching at 1178 and raises the common-live matching from 936 to 942.
Their support rank after directed-DM contraction is 5, while the union of
their newly exposed common-live incidences has contracted graphic rank 12.

By contrast:

* applying all 36 individually common-improving circuits gives common-live
  matching 959, but lowers packet matching from 1178 to 1125;
* applying all 715 circuits lowers packet matching to 569 and common-live
  matching to 308.

So raw palette-neutral capacity is highly unsigned.  A perfect matching in
the support-two root graph is not a topological connector theorem.

There are 220 circuits that add at least one incidence crossing the baseline
Hall cut, but only 36 improve the matching.  Thus merely crossing the current
DM shore is not sufficient: simultaneous deletions and other tight shores
must be protected.

## 4. Exact exchange formula once a chronology forest exists

Suppose a later artifact supplies an actual selected transition graph (P).
Let a circuit delete the selected arcs (D) and insert selected replacement
arcs (A).  Put (R=P\setminus D), and let (r_G(E)) denote graphic rank.
Then

\[
c((P\setminus D)\cup A)-c(P)
=
\bigl(r(P)-r(R)\bigr)-r_R(A).
\tag{4.1}
\]

This follows immediately from (c(G)=|V|-r(G)) and

\[
r(R\cup A)=r(R)+r_R(A).
\]

Consequently the circuit is component-reducing exactly when

\[
r_R(A)>r(P)-r(R).
\tag{4.2}
\]

Equation (4.2) is the correct SCD-chain-splice sign.  The first term is the
rank lost when old chain links are cut; the second is the independent rank of
the cross-chain links after the retained components are contracted.

The static rooted factor does not specify (P,D,A), so (4.2) cannot yet be
evaluated for its circuits.

## 5. Minimal extra artifact

To turn the DM audit into a genuine topology audit, one must freeze:

1. a selected root-owner attachment state for every represented root;
2. selected literal state arcs of indegree and outdegree at most one forming a
   directed path/cycle forest (P);
3. named unmatched endpoints when the forest is partial;
4. for each circuit, the selected replacement arcs (A) and the old selected
   arcs (D) it invalidates.

With those four rows, (4.1) gives an exact merge/preserve/split sign and a
standard graphic-matroid oracle gives the maximum component-reducing bank.
Without them, neither a maximum common-live matching nor its DM decomposition
defines chronology components.

## 6. A clean sufficient DM-splice lemma

The following is the right pre-chronology exchange statement.

### Lemma 6.1 (protected alternating augmentation)

Let (M) be a maximum matching in the common-live graph.  Suppose a
palette-neutral circuit preserves all edges of (t) pairwise vertex-disjoint
baseline alternating paths and adds (t) closing incidences that turn them
into vertex-disjoint augmenting paths.  Then the new common-live matching has
size at least (|M|+t).

If several root-disjoint circuits have disjoint alternating witnesses, their
gains add.

### Proof

Symmetric-difference (M) with the (t) disjoint augmenting paths.  Each path
increases matching cardinality by one, and disjointness makes the toggles
commute.  Palette neutrality is orthogonal and is already certified by each
support-two circuit.  ∎

The five Pareto circuits above are a finite witness that this protected
augmentation mechanism is nonempty and composable.  They do not establish a
positive-density theorem.

## 7. Revised SCD-fragmentation verdict

The previous root-perfect bank proves \(\Theta(W)\) raw two-chain exchanges.
This audit shows that only a small signed subbank is immediately useful:

* packet-improving bank rank: 0;
* common-live-improving support matching/rank: 36;
* simultaneously common-improving and packet-nonregressing bank: 5.

Therefore support-two circuits solve the **supply** side of the fragmentation
wall but not the **sign** side.  The remaining all-dimensional lemma is a
protected signed-bank theorem: a positive-density set of palette-neutral
circuits must carry disjoint alternating witnesses and positive relative
graphic rank under (4.2), while regenerating after each serial round.

## 8. Artifacts

* O3 audit:
  `scratch/audit_k17_support2_circuit_dm_gain_20260801.cpp`
* per-circuit exact table:
  `scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/circuit_dm_gain.tsv`
* aggregate audit:
  `scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/circuit_dm_gain.audit.json`

The audit scope deliberately says `no chronology merge/split claim`.

Frozen SHA-256 values:

* O3 audit source:
  `14526ebf096bf7476799006d0dc25f1bb6d5f7db735b82798970fb2e2ab6db25`;
* per-circuit table:
  `642cb1317980fcb0b4edf9e8ab3b312a31832cbe37662e99f9790b524032ea73`;
* aggregate JSON:
  `87f354f45dd161807b3624b4029255089845bb485cca44a00e2e767b07884080`.
