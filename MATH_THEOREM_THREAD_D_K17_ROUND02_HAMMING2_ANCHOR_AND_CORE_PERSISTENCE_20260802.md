# K17 round02: Hamming-two anchor completeness and residual-core persistence

**Date:** 2026-08-02  
**Status:** exact finite reduction for the frozen round02 one-for-one recut
face; the 12-by-12 resource ledger is independently replayed and its 65
compatible exact-q1 formulas are DRAT-verified UNSAT.  This does not close
the complete Hamming-two face outside the twelve clean escapes.

## 1. Frozen data

The starting bank is
`scratch/threadD_k17_mask114930_core_20260801/round02.bank.tsv`.  Its two
forced owner-mask sockets are

\[
 s=115442,\qquad t=115186,\qquad s\cap t=114930=:c.
\]

The complete one-for-one radius-one audit produced twelve locally clean
non-\(c\) socket escapes.  In authoritative order their side partition is

\[
 T=\{0,1,3,4,6,8,10\},\qquad
 S=\{2,5,7,9,11\}.                                      \tag{1.1}
\]

Their new lower masks are, in the same order,

\[
\begin{split}
&115122,98802,82674,115058,115154,99058,\\
&49650,115378,115170,115410,82418,115426,
\end{split}                                               \tag{1.2}
\]

and are pairwise distinct.

The independent resource replay is
`scratch/audit_threadD_k17_round02_escape_pair_resources_20260802.cpp`.
It reads the literal owner-mask seam ledger rather than serialized SAT
variable numbers.  Its outputs are

* `scratch/threadD_k17_mask114930_core_20260801/socket_escape_pairs.resource.tsv`;
* `scratch/threadD_k17_mask114930_core_20260801/socket_escape_pairs.resource.audit.json`.

## 2. Exact old-fan pair ledger

There are \(\binom{12}{2}=66\) unordered pairs.  Exactly one is not a legal
two-recut bank: rows 8 and 11 are the alternatives `12065->12067` and
`12065->12066` of the same base piece 2251.  Hence there are 65 compatible
pairs.

There are 35 formal \(S\)-by-\(T\) pairs and 34 compatible ones.  For every
compatible cross-side pair, choose one advertised arm at `s` and one at `t`.
The replay proves simultaneously that

1. their lower colours are distinct;
2. their outside owner masks are distinct;
3. their outside physical pieces are distinct; and
4. the two central pieces are distinct.

Thus every one of the 34 compatible cross-side pairs has a literal
two-new-arm rainbow matching saturating `s,t`.

The other 31 pairs are same-side.  Every individual row already has a
literal witness consisting of its new non-\(c\) arm and a surviving old
\(c\)-arm at the opposite socket.  The opposite witnesses use bases 913
and 1099, while none of the twelve recuts changes either base.  For two
different recut bases the first row's new arm and selected colour also
survive the second recut.  Therefore all 65 compatible pairs destroy the
*old* `114930` dual-fan certificate.

This is only an old-core statement.  It explains why merely pairing one
`S` row with one `T` row is not a q1 theorem.

### Theorem 2.1 (the clean-escape pair face is closed)

Every one of the 65 compatible pairs preserves all 265 relaxed local rows.
Their 65 exact orientation-coupled q1 formulas are UNSAT, and every retained
proof is accepted by the DRAT checker.  Consequently no pair of the twelve
certified clean socket escapes completes q1.

The solve and proof manifests are

* `scratch/threadD_k17_round02_escape_pairs_20260801/summary.tsv`, SHA-256
  `b2cdcece539162e9a0eee4ad4ebcdfc0597cc075e0b8732674511753add8a39b`;
* `scratch/threadD_k17_round02_escape_pairs_20260801/drat_summary.tsv`,
  SHA-256
  `006c2c09177248228cf40a20d78472ee28abcc581c95308050546f3db6a1f3f3`.

The independent lightweight manifest audit authenticates a bijection
between the 65 pair keys and the 65 solve rows, canonically hashes all 65
local banks, and cross-checks all CNF hashes against the checked-proof
ledger.  It is
`scratch/audit_threadD_k17_round02_escape_pairs_manifest_20260802.py`, with
output
`scratch/threadD_k17_round02_escape_pairs_20260801/independent_manifest.audit.json`.
It does not rerun SAT or DRAT, so the checked proof ledger remains the
load-bearing logical certificate.

## 3. The residual proof libraries

The current proof-specific compact library
`scratch/threadD_k17_round02_escape_core_library_20260801` has named lower
rows

\[
\begin{array}{c|c|c}
\text{rows}&\text{named lower masks}\\ \hline
\{0\}&118996\\
\{1,2,3,4,7,8,9,10\}&115308\\
\{5\}&115308,117348\\
\{6\}&14820\\
\{11\}&87145.
\end{array}                                                \tag{3.1}
\]

An independently extracted alternative owner-graph library is also valid;
it gives, among other certificates, the `35275/35786` and `31844/32352`
bow ties recorded in
`scratch/threadD_k17_round02_socket_escape_cores_20260801`.  Different
verified cores of the same child are assets: a second recut must hit every
retained certificate, not merely one convenient extraction.

For the `118996` core the owner path is

\[
119508-127188-119004-119028,
\]

with nonadjacent forced sockets `127188,119028`.  For the `115308` fan the
forced sockets are `115310,119404` and the physical leaf bank is the same
in all eight listed children (row 5 merely has one extra pendant elsewhere).

An identical single-child owner graph is **not**, by itself, a pair no-go.
The second recut can select a lower colour that was absent in the first
child and thereby activate a previously latent seam into a forced socket.
It can also change an endpoint row without changing the displayed old
edges.  A pair is prunable only after the following incidence test.

## 4. Safe multi-core persistence

For a verified UNSAT core \(K\), let

* \(P(K)\) be its physical pieces and orientations;
* \(O(K)\) be the directed tail rows occurring in it;
* \(I(K)\) be the directed head rows occurring in it; and
* \(C(K)\) be its lower-colour rows.

All of these are literal owner-mask resources, not legacy variable numbers.

### Theorem 4.1 (core-persistence pruning)

Let \(D_i\) be one of the twelve single-recut banks and let \(K_i\) be any
verified UNSAT core of its exact q1 formula.  Add a compatible second recut
\(j\).  If, after rebuilding the joint bank,

1. every state in \(P(K_i)\) is unchanged;
2. the complete legal selected-colour seam set in every row of
   \(O(K_i)\cup I(K_i)\) is unchanged; and
3. the complete legal seam set of every colour in \(C(K_i)\) is unchanged,

then the joint q1 formula is UNSAT.

#### Proof

Under items 1--3, every orientation, endpoint, colour and at-most-one
constraint used by \(K_i\) occurs in the joint formula with identical
incidence, up to a renaming of seam and sequential-counter variables.
Consequently the verified core embeds in the joint formula.  A formula
containing an UNSAT subformula is UNSAT. \(\square\)

It suffices that **one** verified core of either child persists.  Therefore
an exact second-recut search need rebuild/solve only pairs that hit every
retained core certificate of both single children.  For a dual-fan core
with locked sockets \(u,v\) and sole colour \(q\), the row test reduces to
the two-socket rainbow rank condition

\[
 \rho_{D_i+j}(\{u,v\})=2,                                  \tag{4.1}
\]

or a literal role relocation.  In owner masks, a prospective new arm to
`u` through endpoint `w` is relevant only if

\[
 |u\cap w|=8,\quad |u\cup w|=10,
\]

the exact two-block residence predicate holds, and the lower mask
`u& w` is selected in the **joint** bank.  This is the compact
cross-activation test missing from a one-child provider count.

No named-core signature in (3.1), without this joint row check, proves a
pair no-go.

## 5. Exact Hamming-two anchor lemma

There are 16,667 one-for-one recuts.  A noncentral recut leaves both old
central states fixed.  For such a recut \(a\), call a raw seam an endpoint
state `w` which is Johnson-legal and two-block-resident with `s` or `t`,
before requiring its lower mask to be selected.

### Lemma 5.1 (raw-anchor completeness)

Let \(a,b\) be compatible recuts and suppose their joint bank destroys the
old `114930` dual fan.  Then at least one of the following occurs.

1. One of \(a,b\) is one of the nine recuts of central bases 1834 or 1835.
2. One single child already has a selected non-`114930` socket seam.  This
   includes dirty single children; the other recut may repair their local
   zero rows.
3. One recut, say \(a\), exposes a raw seam of lower mask \(q\) at `s` or
   `t`, the mask \(q\) is unselected after \(a\) alone, and the other recut
   \(b\) selects \(q\).

For noncentral recuts no additional direct-`st` case exists.

#### Proof

With both central states fixed, a joint breaker which is not a role change
must contain a non-`114930` seam incident with `s` or `t`, unless it is the
direct `st` seam.  The noncentral seam's other endpoint state is changed by
at most one recut, say \(a\).  Its lower mask is either already selected
after \(a\), giving item 2, or is selected only by \(b\), giving item 3.
The direct `st` seam has both endpoint states fixed, colour `114930` already
selected, and a fixed failed residence test; remote recuts cannot create it.
If a central state changes, the recut is among the nine alternatives in
item 1. \(\square\)

The published twelve rows are only the **locally clean** part of item 2.
Thus the unconditional Hamming-two anchor family is not merely
`12+9`.  It is

\[
\boxed{\text{all nine central recuts}
\;\cup\;\text{all selected-visible recuts (clean or dirty)}
\;\cup\;\text{all raw-endpoint/lower-supplier pairs}.}      \tag{5.1}
\]

The implementations

* `scratch/audit_threadA_k17_round02_dualfan_hamming2_projection_20260802.cpp`,
* `scratch/audit_threadA_k17_round02_hamming2_anchor_completeness_20260802.cpp`,
* `scratch/sweep_k17_round02_anchored_two_recuts_20260802.cpp`

realize this partition.  Independent source audit found the multiplicity
ledger, supplier lookup, pair deduplication and dirty-visible branch
logically complete.  The quantity named `supported_escape` is deliberately
overinclusive: it records a selected noncore incidence, not necessarily a
resource-disjoint rank-two witness.  This is safe for completeness but must
not be reported as an exact breaker count.

## 6. Smallest remaining pair classes

Inside the certified twelve-row face, the 65 compatible pairs all survive
the old-fan screen but Theorem 2.1 closes every one at exact q1.  For a new
pair catalogue, the reusable solver-independent pruning order is:

1. test every available proof-specific core by Theorem 4.1;
2. for the simple fans, test the joint owner-mask rank (4.1);
3. rebuild exact q1 only when the pair hits every retained core; and
4. only after q1-SAT, replay all 265 local rows and the downstream residence,
   deeper-shadow, topology and compiler gates.

Thus the smallest live faces are not another pairing of these twelve rows,
but the still-unclosed dirty-visible/latent/central Hamming-two branches or
a genuine C6/C8/q4 rethread.  In the complete Hamming-two face, first
evaluate the three anchor families
in (5.1).  A conditional sweep of the twelve clean visible anchors plus the
nine central recuts is useful, but becomes a complete theorem only after the
dirty-visible and latent raw/supplier branches are either included or
jointly excluded.

## 7. Scope

The theorem concerns exactly the frozen round02 one-for-one recut face.  It
does not cover adding a cut, deleting a cut with compensation, C6/C8 factor
rethreads, split/merge moves, another dense bank, or the full `k=17`
construction.  A pair which destroys every named core is a candidate, not a
certificate; exact q1 and all downstream literal gates remain mandatory.
