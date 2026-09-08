# K17 singleton-hole extremal bank and the protected resident-completion gate

Date: 2026-08-02  
Status: exact structural theorems and read-only authenticated audits.  The
literal “proper-block family always has transversal at most 13” statement is
refuted.  The stronger missing-target statement under **global** depth-three
residence remains open.  A later protected-completion lane proved that the
**orbit closure** of this bank is residence-inconsistent on the frozen
marker58 equivariant face; see
`MATH_THEOREM_K17_Y61423_ORBIT_CLOSED_PROTECTED_BANK_RESIDENCE_CORE_NOGO_20260802.md`.
The unrestricted non-equivariant physical completion remains open.

## 0. Outcome

Let `F` be an owner-once exact-rank-eight-facet Hamilton factor on the K17
rank-nine layer.  If rank 13 is complete but a rank-14 target `Y` is missing,
the clean-block theorem forces fourteen distinct clean blocks with persistent
holes

\[
                            \{y\},\qquad y\in Y.          \tag{0.1}
\]

There is no incompatibility between (0.1) and the owner/facet/q1 resources.
In the authenticated residence-1666, all-upper-complete owner-once factor:

* 357 of the 680 physical rank-14 targets already have all fourteen
  singleton-hole blocks among their proper clean blocks;
* 17 targets admit one such block for every coordinate while avoiding every
  owner lying in an incumbent positive run of length two or three; and
* target `Y=61423` has a protected fourteen-block bank using 76 clean owners
  and 90 distinct rank-eight facets whose entire incident-edge support forces
  **zero** short positive run.

Thus the proper-hole subfamily for `Y=61423` has transversal number fourteen,
strictly greater than `r+4=13`, while being locally compatible with owner
degree, exact facets, q1 geometry, and the residence Horn clauses.  This
refutes any theorem bounding the transversal of the nonempty/proper block
subfamily from those local rows.

It does **not** yet give the desired missing-target counterexample.  The
ambient factor has 1,666 short runs elsewhere and twelve other Y-clean blocks
whose union is all of `Y`.  The exact remaining question is global:

> Can the rest of the factor be completed/rethreaded to depth-three residence
> while protecting the 90-edge singleton bank and destroying every full-Y
> clean block?

That protected completion problem, rather than singleton-hole supply or a
local facet/residence count, is the genuine frontier.

## 1. Exact run identities forced by lower-facet bijectivity

The lack of a scalar contradiction is structural, not merely empirical.

Let `k=2r-1`, and let a Hamilton cycle through all rank-`r` owners use every
rank-`r-1` intersection facet exactly once.  Fix a coordinate `x`, and let
`a_x` be the number of positive runs in its cyclic owner trace.  The number
of zero owners is `binom(k-1,r)`.  Among the cycle edges whose intersection
misses `x`,

* `binom(k-1,r)-a_x` are internal zero-zero edges; and
* `2a_x` are positive/zero boundary edges.

Exact facet use says their total is `binom(k-1,r-1)`.  Hence

\[
 a_x=\binom{k-1}{r-1}-\binom{k-1}{r}
    =\frac1r\binom{2r-2}{r-1}=\operatorname{Cat}_{r-1}.  \tag{1.1}
\]

There are `binom(k-1,r-1)=r Cat_(r-1)` positive owner occurrences and
`binom(k-1,r)=(r-1) Cat_(r-1)` zero occurrences.  Therefore every coordinate
has exact average positive- and zero-run lengths

\[
                              r\quad\hbox{and}\quad r-1.  \tag{1.2}
\]

At K17 these are 1,430 positive runs per coordinate, with average lengths
nine and eight.  The required positive floor is only four.  Exact facet
arithmetic therefore leaves ample scalar room for depth-three residence; it
cannot exclude the singleton bank.

## 2. What a missing rank-14 target would require

Fix a rank-14 set `Y`.  It has

\[
                         \binom{14}{9}=2002             \tag{2.1}
\]

clean owners.  Let its maximal clean blocks have unions `U_B` and nonempty
holes `H_B=Y-U_B` when `Y` is missing.

If all rank-13 targets are covered, the hole-transversal theorem gives

\[
                             \tau(\{H_B\})>13.           \tag{2.2}
\]

A nonempty-set hypergraph on fourteen vertices has transversal number
fourteen exactly when it contains all fourteen singleton edges.  Thus (2.2)
is equivalent to (0.1).  Each singleton block has union `Y-{y}` and therefore
contains at least five rank-nine owners: one starting owner plus at least
four Johnson insertions.

The elementary resource lower bounds are consequently only

\[
            14\cdot5=70\text{ clean owners},\qquad
            14\cdot(5+1)=84\text{ incident facets}.      \tag{2.3}
\]

These are tiny beside (2.1) and the 3,003 available rank-eight facets inside
`Y`.  The general exact-facet bound allows as many as

\[
                    \binom{14}{8}-\binom{14}{9}=1001     \tag{2.4}
\]

clean blocks.  Residence allows still more.  Hence no scalar version of the
clean-block count can rule out (0.1).

## 3. Authenticated full-factor census

The audited factor is the strict clean-1666 C16 deep control

```text
/home/amodo/or15/work/qa_k17_endpoint_deep_incremental_20260802_quotientaudit/
  validated_clean1666_c16_deep1717_391/factor.tsv
SHA256 ff75194a4c071eb1d3c82269e482a9d0175e0356b0f6ad177daa9d7a9b5f8009
```

It is a simple owner-once physical Hamilton cycle with exact rank-eight
facets and complete q1/upper ranks, but it has 1,666 positive runs shorter
than four.  A read-only H100 census over all 680 rank-14 targets returned

```text
targets=680 covered=680
all_singleton_targets=357
all_singletons_badfree=17
shortest_singleton_total=75 shortest_singleton_max=7
shortest_badfree_y=61423
shortest_badfree_total=76 shortest_badfree_max=8
```

“Badfree” means that for each of the fourteen singleton holes there is a
clean component containing no owner from any incumbent length-two or
length-three positive run.  This already shows that the singleton paths are
not themselves a consequence of the current residence defects.

The census source is

```text
a784e2c54dbc50e6e60dcfb07e91c8d152f5211759b110274866e8752d3073e8
  scratch/census_k17_rank14_clean_block_singleton_holes_20260802.cpp
```

## 4. Exact protected-bank residence audit

Avoiding bad owners is suggestive but not by itself the correct partial
residence test: two selected boundary edges around an unselected dirty owner
could still force a short run.  The second audit therefore uses edge support.

For every incumbent short positive run, record the complete edge interval
from its entering boundary through its leaving boundary.  A partial selected
edge bank forces that bad run exactly when it contains every edge in this
interval.  For `Y=61423`, choose one singleton-hole component for every
coordinate and include **every** factor edge incident to its clean owners.
The audit selects the components jointly and rejects any choice whose union
contains a complete short-run edge interval.

It returned

```text
PASS_K17_RANK14_SINGLETON_BANK_PARTIAL_RESIDENCE_AUDIT
target=61423 clean_components=815 empty_blocks=12
singleton_blocks=14 total_owners=76 max_block=8
support_edges=90 distinct_facets=90
incumbent_short_runs=1666 forced_short_runs=0 search_nodes=15
block_lengths 5 5 5 5 7 5 5 6 5 5 5 5 8 5
```

Thus the selected support is a literal 90-edge protected bank satisfying:

1. all owner capacities, because it is a subgraph of the owner-once factor;
2. all lower-facet capacities, with 90 distinct rank-eight facets;
3. literal Johnson/q1 geometry on every selected edge;
4. all fourteen singleton-hole unions; and
5. the exact partial positive-residence condition—no run of length one,
   two, or three is forced.

Here “selected support” means exactly the 90 physical edges.  It does not
mean their full `Z_17` orbit closure.  The latter adds translated edges and is
inconsistent with residence by the later three-clause core theorem cited in
the status paragraph.

Equivalently, after orienting the fragments as in the incumbent, the compact
Horn residence module has a consistent partial assignment on this bank.
Endpoint witnesses and their one-/two-step propagations cannot reach an
accepting conflict because such a conflict would be precisely one of the
fully selected short-run edge intervals checked above.

The audit source and frozen JSON are

```text
e90d369641cbc8209f025abd5ebe685922ba0fa6e9792a3109a74f7bf0b5e7e7
  scratch/audit_k17_rank14_singleton_bank_partial_residence_20260802.cpp
b2685a3558354c7e65b4ca92832bcf3de5b96354458bdcf78adca8486ff3a42c
  scratch/k17_rank14_singleton_bank_partial_residence_20260802.audit.json
```

The JSON has its own file hash and binds the displayed factor/source hashes.

## 5. Exact logical conclusion

There are two different transversal claims.

### Claim A: every nonempty/proper clean-block subfamily has small transversal

This is false.  In the authenticated exact owner-once q1 factor, discard the
twelve full-union blocks for `Y=61423`.  The remaining proper-block family
contains every singleton hole, so its transversal number is fourteen.  The
90-edge subfamily exhibiting those holes is locally residence-compatible.

### Claim B: if the entire factor is globally depth-three resident and `Y` is
missing, then the complete hole family has transversal at most thirteen

This is not resolved by the audit.  The incumbent is not globally resident,
and its twelve empty holes make `Y` covered.  A proof of Claim B must use a
global interaction between completion of all residence defects and survival
of full-Y blocks.  It cannot follow from:

* exact owner/facet counts;
* q1 geometry;
* the singleton blocks themselves;
* any scalar residence ledger; or
* the local Horn residence constraints on the protected bank.

Conversely, a counterexample requires a protected completion theorem:

> Complete the complement of the 90-edge bank to an owner-once exact-facet
> Hamilton cycle with positive run floor four, while ensuring that every
> Y-clean component outside the bank has a nonempty persistent hole.

This is a substantially narrower target than a fresh K17 factor search, but
it is still a global completion problem.  No existing theorem guarantees it,
and no duplicate SAT instance was launched here.

## 6. Relation to the active K17 master

The frozen v3+rank11 formula still contains union562.  The canonical sound
residence bank has advanced to union612.  Both exact 1,800-second v3+rank11
solver lanes timed out `UNKNOWN`; neither produced a SAT model nor an UNSAT
proof.  Those timeouts give no evidence for or against the protected
completion above.

The correct next theorem-level move is one of:

1. a protected extension theorem for locally residence-consistent path
   banks in the middle-levels incidence cycle; or
2. a global invariant proving that every resident completion of this bank
   necessarily retains at least one full-Y clean component.

The singleton-hole/transversal supply itself is no longer the unknown row.
