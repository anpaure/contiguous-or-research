# K17 promoted-packet deep guard and exact two-recut composition

Date: 2026-08-02  
Lane: AD  
Status: proved compositional guard theorem; fail-closed deterministic evaluator
implemented and regression-audited.  No q1 search was run.

## 0. Result and scope

This note rebases on

```text
MATH_THEOREM_AD_K17_DENSE_REFINEMENT_RESIDENCE_AND_ALLWIDTH_GUARDS_20260801.md
```

and on the exact radius-one/radius-two facts:

* the twelve one-recut socket escapes are q1-UNSAT;
* their 65 compatible visible-visible pairs are q1-UNSAT;
* the live next face is the unfiltered geometry-by-colour-supplier Hamming-two
  catalogue, which includes jointly activated seams invisible in both unary
  selected atlases.

The new conclusions are:

1. A jointly activated two-recut has an exact order-free deep-shadow guard.
   Removing the two old cuts cannot destroy a retained internal witness; only
   the two new cuts can.  Consequently it can lose at most 162 previously
   internal upper masks in total, with the exact layer bounds in (3.3).
2. This 162 bound is a cut-bank statement.  Once a q1 rematching is selected,
   the correct support is the complete occurrence-labelled set of reference
   adjacencies absent from the final chronology.  It must be recomputed.
3. A promoted complete chronology admits an exact, finite, fail-closed audit:
   literal owner/Johnson/q1 replay, exact cyclic depth-three product residence,
   exact accumulated-union decks at ranks 11 through 17, exact retained-old-
   witness residual, and an explicit cross-deck inclusion certificate for the
   81-per-active-edge bound.
4. The completed unfiltered raw central-seam/supplier projection has no
   nonanchor candidate pair: its pair TSV consists only of the header.  This
   narrows the live Hamming-two face to the guarded anchor sweep, but it is
   not q1 closure and supplies no complete chronology.  Therefore no latent
   row receives a global residence or deep-guard PASS in this note.  The
   evaluator is ready for the first materialized two-recut/C6/C8 output; it
   does not duplicate q1 solving.

The implementation is

```text
scratch/audit_ad_k17_promoted_candidate_deep_guards_20260802.cpp
SHA256 dc68dd7d948e5c0de92bfac330eb552edd45489364f3d43f257059a37a25e9a3
```

## 1. Literal chronologies and old witnesses

Let (G) be a maximum-degree-two reference graph on a set (V) of distinct
rank-nine owner occurrences in ([17]).  Let (H) be a second literal
maximum-degree-two graph on the same owner occurrences.  Every edge of both
graphs is required to be a Johnson edge.  Put

\[
                         A=E(G)\setminus E(H).             \tag{1.1}
\]

The word *active* below always means an occurrence-labelled edge in (1.1).
It does not mean a cut ID, a lower-colour mask, a packet ID, or a projected
socket.

For an upper mask (U), let ({\cal W}_G(U)) be the family of literal path or
cyclic-interval witnesses in (G) whose owner union is (U).  Define the
retained-old deck by

\[
 {\cal R}(G,H)=
 \{U:\exists I\in{\cal W}_G(U),\ E(I)\cap A=\varnothing\}. \tag{1.2}
\]

### Theorem 1.1 (exact retained-witness criterion)

A literal old witness survives as an old path in (H) if and only if it is
counted by (1.2).

#### Proof

If (E(I)\cap A=\varnothing), every edge of the old path (I) belongs to
(H).  Since (H) has maximum degree two, no internal vertex of this path
can leave it.  The same owner sequence is therefore consecutive in (H),
possibly reversed, and has the same union.  Conversely an old witness is
retained precisely when all of its old internal adjacencies remain in (H),
which is the condition in (1.2).  QED

Failure of (1.2) is an old-channel residual, not necessarily a final hole:
new seams can redeliver (U).

## 2. Exact 81-per-active-edge charge

Fix (e\in A).  Cut its reference component at (e).  The unions of suffixes
on one shore of the cut form a nested chain with at most nine distinct states;
the prefix unions on the other shore form another such chain.  Let (X_e) be
their pairwise union deck.

### Theorem 2.1 (cross-deck inclusion and bounds)

\[
 {\cal D}(G)\setminus{\cal R}(G,H)
       \subseteq\bigcup_{e\in A}X_e,                    \tag{2.1}
\]

and

\[
 |X_e|\le81.                                             \tag{2.2}
\]

At rank (9+q), (q=1,\ldots,8),

\[
 \left|X_e\cap { [17]\choose 9+q}\right|\le(q+1)^2.    \tag{2.3}
\]

In particular, over any subset of upper ranks,

\[
 |{\cal D}(G)\setminus{\cal R}(G,H)|\le81|A|.           \tag{2.4}
\]

#### Proof

Choose any old witness (I) not retained by (1.2).  It contains an active
edge (e).  Relative to the cut at (e), (I) is a suffix on one shore
followed by a prefix on the other, so its union lies in (X_e).  Each nested
union chain starts at rank nine and can strictly grow at most eight times,
giving at most nine states and hence (2.2).  At target rank (9+q), only the
first (q+1) states of either chain can participate, giving (2.3).  Taking a
union over (A) proves (2.4).  QED

The 81 is a total bound, not the sum of the layer bounds.  The implementation
constructs every (X_e), checks the per-edge total and layer bounds, and
verifies (2.1) mask by mask.  It does not merely compare two scalar counts.

For a bare alternating C6 which deletes exactly three reference edges and
changes no others, (2.4) gives 243.  For a bare C8 deleting four, it gives
324.  These are conditional support counts.  If the final q1 rematching
deletes other old adjacencies, the evaluator charges the complete final
(A), not three or four.

## 3. The jointly activated two-recut theorem

Let (F) be a fixed old owner factor and (C_0) a cut set.  Write
({\cal I}(F,C)) for the union of the interval-OR decks internal to the
pieces of (F-C).  Suppose two distinct recuts produce

\[
 C_1=(C_0\setminus\{c_1,c_2\})\cup\{d_1,d_2\}.          \tag{3.1}
\]

No unary cleanliness or unary socket visibility is assumed.

### Theorem 3.1 (exact two-recut retained guard)

For every target (U),

\[
 U\in{\cal I}(F,C_1)
 \iff
 \exists I\in{\cal W}_F(U):
       \operatorname{int}(I)\cap C_1=\varnothing.       \tag{3.2}
\]

Moreover,

\[
 {\cal I}(F,C_0)\setminus{\cal I}(F,C_1)
       \subseteq X_{d_1}\cup X_{d_2}.                   \tag{3.3}
\]

Thus at most 162 previously internal upper masks are lost in total.  At
ranks 11 through 17 the respective bounds are

\[
             18,\ 32,\ 50,\ 72,\ 98,\ 128,\ 162.       \tag{3.4}
\]

#### Proof

An old interval is internal after cutting exactly when none of its internal
gaps is cut, proving (3.2).  If a witness is internal under (C_0), it
already avoids (c_1,c_2).  Removing those cuts cannot destroy it.  If it
fails under (C_1), it crosses (d_1) or (d_2), proving (3.3).  Apply
Theorem 2.1 to the two new cuts to obtain (3.4).  QED

This theorem is exactly adapted to a latent geometry-by-colour-supplier
activation: one recut may create raw seam geometry while the other supplies
its selected lower colour, but their internal old-witness loss still has no
hidden second-order term.  The jointly activated seam can only add actual
interval witnesses.  Product residence and final q1 matching remain separate.

The 162 bound ceases to describe the final object if a subsequent q1
selection omits additional incumbent adjacencies.  Then (1.1)--(2.4), with
the complete final (A), are the exact statement.

## 4. Exact depth-three product residence

For each coordinate use the six-state automaton

\[
 Q_3=\{0,1,2,3,{\mathsf L},\bot\},                       \tag{4.1}
\]

where a zero closes a run in states 1,2,3 into (ot), and a fourth one
moves state 3 to ({\mathsf L}).  Concatenation is composition of transition
maps.

### Theorem 4.1 (assembled guard)

For a complete oriented cycle, depth-three residence is equivalent to the
absence, in every cyclic coordinate trace, of (0,1^j,0) with
(1\le j\le3).  For a path it is equivalent only after its exterior collar
states are supplied; with clipped ends one may certify internal runs but not
an arbitrary later join.

For an unordered piece bank, internal residence of each piece is necessary
but not assembled residence.  In particular, two individually failing
contextual recuts may pass jointly after their boundary states change, and
two individually resident pieces may form a short run when joined.

Every literal assembled failure (0,1^j,0) yields an occurrence-specific
lazy no-good on at most (j+1\le4) selected adjacencies, guarded by the full
cut/orientation activation state.

#### Proof

This is the exact transition product: a zero reaches (ot) precisely when
it closes a positive run of length 1, 2 or 3.  A cyclic zero supplies a break;
an all-one trace is accepted.  A path has an unclosed state at either end and
therefore needs its collars.  The bad substring has (j+1) adjacencies, at
least one of which must change.  QED

Thus a raw two-recut/C6/C8 catalogue row without its complete selected
chronology must be labelled `UNBOUND` or `PENDING_JOIN`, never globally
resident.

## 5. Fail-closed evaluator contract

The evaluator accepts either:

1. a complete incidence 2-factor with exact header
   `lower<TAB>owner<TAB>protected`; or
2. a complete ordered chronology with exact header
   `component<TAB>position<TAB>closed<TAB>owner`.

Every other input, including the twelve-row socket table or a latent cut
projection, exits fail-closed with code 2.

It then independently verifies:

* exactly all 24,310 distinct rank-nine owners;
* every selected adjacency is Johnson;
* exact lower-q1 and complete upper-q1 replay;
* exact cyclic depth-three residence, coordinate by coordinate;
* exact old, retained-old and final interval-union decks at every mask of
  ranks 11 through 17, including cyclic wrap intervals;
* (A=E(G)\setminus E(H)) from literal owner pairs;
* every active (X_e), the per-edge 81/layer bounds, and the maskwise
  inclusion (2.1);
* every new final loss and every healed intrinsic old hole.

The target certificate has exactly

\[
 {17\choose11}+\cdots+{17\choose17}=21778              \tag{5.1}
\]

data rows, plus its header.  Each target is classified as retained,
casualty-redelivered, casualty-final-hole, intrinsic-healed, or intrinsic-
still-hole.

A closed candidate receives `PASS_DEEP_GUARDS` only if assembled residence
passes, q1 replay passes, and no target covered by the reference chronology
is lost from the final deck.  Intrinsic reference holes may remain; they are
reported separately.  An open chronology with no internal bad run is only
`PARTIAL_OPEN_Q1_AND_BOUNDARY_UNRESOLVED`: its closure-supplied q1 edge(s)
and exterior collar states are both still undecided.  Missing owner occurrences,
non-Johnson edges, malformed headers or unsupported local packet rows fail
before any positive status.

The direct accumulated-union enumeration uses first-arrival events.  From a
rank-nine start there are at most eight strict union changes, so all cyclic
and linear decks are reconstructed in (O(17W)) event work rather than by
quadratic interval enumeration.

## 6. Authenticated regressions

All regressions were deterministic local audits, not searches.

### 6.1 Identity factor

Using the authenticated reference as its own candidate reproduces exactly:

```text
components                  7
active old edges            0
depth-3 bad runs            5783 = 3073 + 2710
old/final holes r11..r17    1502,295,9,0,0,0,0
retained casualties         0
status                      REJECT_DEPTH3_RESIDENCE
```

This independently recovers the frozen residence and upper-deck ledger.

### 6.2 Protected C6 row 144

Candidate:

```text
scratch/threadA_k17_c6_dynamic2_20260801/row144.factor.tsv
SHA256 af235ad2b631e4dd56f686e823571d043c1bfd482cccb924ae86ba9df0be67fa
```

Replay gives:

```text
components                  5
active old edges            3
depth-3 bad runs            5780
retained casualties         0 <= 243
intrinsic holes healed      3 (one rank-11, two rank-12)
new final losses            0
status                      REJECT_DEPTH3_RESIDENCE
```

The component/run/hole values agree exactly with the independently frozen
row-144 materialization.  This is also a literal example where a C6 has
nontrivial topology and upper gains but fails the residence guard.

### 6.3 Large-active-support stress replay

Candidate:

```text
scratch/r2_k17_reset_open_ml9_ffactor_20260801/run.cut0.factor.tsv
SHA256 74c93d0387e9e833d145464264d7121ec89971f7cb7f509127b192c5b92ee4fa
```

Replay has 23,105 active old edges and 19,954 retained casualties.  Every
casualty lies in the explicitly reconstructed active cross-deck union.  The
candidate has 10,067 new final losses and 14,687 bad residence runs, so it is
correctly rejected.  This stress test exercises the inclusion certificate,
not only the zero-active identity case.

The frozen regression bundle is

```text
scratch/ad_k17_round02_synergistic_two_recut_guards_20260802/
```

with manifest

```text
regression_manifest.audit.json
```

The manifest binds all input/output hashes and records the unsupported-table
negative test.

An independent final source audit checked the linear/cyclic first-arrival
enumeration, retained-segment splitting, active cross-deck wrap indices,
maskwise inclusion, layer bounds, depth-three scan and status ordering.  It
identified one harmless-but-misleading open-path status label; after renaming
that state to `PARTIAL_OPEN_Q1_AND_BOUNDARY_UNRESOLVED`, the audit reports
PASS on source SHA `dc68dd7d948e5c0de92bfac330eb552edd45489364f3d43f257059a37a25e9a3`.

## 7. Exact remaining boundary

The completed read-only H100 projection reports

```text
recuts                              16667
raw socket seams                   733024
off-tight raw socket seams         732950
nonanchor supported unary escapes       0
nonanchor candidate pairs               0
nonanchor joint zero-265/socket pairs    0
```

with remote frozen hashes

```text
latent_join.audit.json   0ee2c01a938b58eec8cb9b26161fcf3defbaf92a8f0ab4211b6c0b97bb09e284
latent_pairs.tsv         9c80a03c0beabc704bd18ecd2d16a02f7511ff22bdd95ea4ebc0f04a300d447e
latent_recuts.tsv        8b8769f4d333a0b3fcdf6fb292c1a9af715e390e1ad310070e3914071fb65f69
```

The exact scope is the nonanchor raw central-seam geometry-by-new-cut-colour
supplier projection implemented by source SHA
`a16ed3687ff938f4b3f9cc34d10b4ea2e43896fa75ec9beb2073c046964b3d23`.
It does not close pairs containing one of the 21 guarded anchors, does not
run q1, and does not materialize an owner chronology.

Proved and implemented:

* exact compositional old-witness guard for jointly activated two recuts;
* total/layer casualty bounds with explicit cross-deck inclusion;
* exact post-materialization product residence and accumulated-union replay;
* fail-closed handling of an unbound cut/packet projection;
* no duplication of the q1 solver.

Not proved:

* that the live latent geometry-by-supplier catalogue contains a q1-SAT row;
* that a q1-SAT row admits a complete oriented chronology passing residence;
* creation of the 1,806 intrinsic old upper holes;
* connectivity/opening, lower pins, source suffix corrections, terminal
  common-cap Hall, or a literal universal OR word.

The next valid use is mechanical: D/A materializes a complete occurrence-
labelled factor or ordered chronology for a promoted two-recut/C6/C8 row;
this evaluator either returns the exact first failing guard and 21,778-row
target certificate, or `PASS_DEEP_GUARDS`.  A raw catalogue row alone is not
promoted and cannot be assigned a global residence verdict.
