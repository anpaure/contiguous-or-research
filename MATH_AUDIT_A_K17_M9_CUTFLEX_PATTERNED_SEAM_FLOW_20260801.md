# Exact flexible-cut audit and patterned seam-flow formulation for the (m=9) SCD forest

Date: 2026-08-01  
Lane: A  
Status: **the cut-flexibility census is independently verified; the resulting global braid is an exact finite-state integral problem and remains open**

## 1. Scope

Let

\[
  C_i=(O_{i,0},\ldots,O_{i,n_i-1})
\]

be the 4,862 directed components of the authenticated (m=9) SCD owner
forest.  Every (O_{i,j}) is a rank-9 subset of a 17-set.  The forest has
24,310 owners and 19,448 edges.  Its upper edge colours
(O_{i,j-1}\cup O_{i,j}) are the complete rank-10 palette, each once; its
lower edge colours (O_{i,j-1}\cap O_{i,j}) are also pairwise distinct.

This note audits only the **minimum cuts which clip every internal positive
owner run of length at most three**.  This is the 1,419-cut depth-3
factorability face.  It is not the 1,634-cut strict-residence ledger for the
maximal source, and it does not impose short-zero-run constraints.

The canonical robust/extendable zero sets used below belong to one particular
cutting.  Their weighted use in Section 3 is therefore a reweighting diagnostic,
not a post-recut provider theorem.

## 2. Exact interval formulation

For a component (C_i), a cut position (c\in\{1,\ldots,n_i-1\}) removes the
edge (O_{i,c-1}O_{i,c}).  If coordinate (x) has an internal positive run

\[
 O_{i,a},O_{i,a+1},\ldots,O_{i,b-1},
 \qquad 0<a<b<n_i,\qquad b-a<4,
\]

then this run becomes boundary-clipped exactly when a cut is placed in the
integer interval ([a,b]).  Let \({\cal I}_i\) be this family of cut-position
intervals, let

\[
 \tau_i=\min\{|P|:P\subseteq\{1,\ldots,n_i-1\},\ P\cap I\ne\varnothing
          \text{ for every }I\in{\cal I}_i\},
\]

and let \({\cal P}_i\) be the family of all size-(\tau_i) transversals.

Because \({\cal I}_i\) is an interval family, the right-end greedy transversal
and the left-to-right disjoint-interval packing have equal size.  Hence
(	au_i) is certified without SAT or floating point.  Enumerating only the
(\tau_i)-subsets gives every minimum pattern.

### Theorem 2.1 (audited minimum-pattern census)

For the authenticated forest:

1. (1,213) components have \(	au_i>0\), and
   \[
     \sum_i\tau_i=1,419.
   \]
2. The cut-count histogram is
   \[
   \tau=0:3649,\quad1:1037,\quad2:149,\quad3:24,\quad4:3.
   \]
3. The sum of the numbers of componentwise minimum patterns is
   \[
      \sum_i |{\cal P}_i|=8,894.
   \]
   Exactly (1,113) components have more than one minimum pattern.  The
   maximum is (144), attained by component 3257.
4. Across all minimum patterns, the union of possible cut colours has size
   4,232 on each q1 shore.  The intersection forced in every minimum pattern
   has size 132 on each shore.
5. Every global choice (P_i\in{\cal P}_i) has 1,419 cuts and therefore
   \[
      4,862+1,419=6,281
   \]
   pieces.

#### Proof

The interval argument above proves the minimum cardinality componentwise.
The independent audit enumerates every subset of that certified cardinality,
tests it against every interval, and then takes unions and intersections of
the corresponding edge-colour sets.  It also independently verifies that the
19,448 original upper edge colours are the complete rank-10 palette and that
all 19,448 lower edge colours are distinct.  The reported counts are direct
integer counts from this enumeration.  No optimization solver is used. ∎

## 3. What the 75/43 weighted seed proves—and does not prove

Let (R_{\rm can}) be the 784 rank-10 colours with no **robust** pairwise
provider in the canonical cutting, and let (E_{\rm can}) be the analogous
322-colour **extendable** zero set.  Give a cut edge cost one when its upper
colour belongs to the chosen reference set and zero otherwise.

### Theorem 3.1 (exact independent weighted minima)

The componentwise independent minima are

\[
 \min_{P_i\in{\cal P}_i}\sum_i|u(P_i)\cap R_{\rm can}|=75,
 \qquad
 \min_{P_i\in{\cal P}_i}\sum_i|u(P_i)\cap E_{\rm can}|=43.
\]

Moreover:

* the 75 and 43 costs are exactly the intersections of the respective
  reference sets with the 132 globally forced cut colours;
* no component incurs cost greater than one at its minimum;
* a single frozen pattern choice attains both minima (the two emitted choice
  tables are byte-identical).

#### Proof

For each component and every enumerated (P\in{\cal P}_i), compute
(|u(P)\cap R_{\rm can}|) and (|u(P)\cap E_{\rm can}|), take the two minima,
and sum over components.  The independent audit obtains histograms
(0^{4787}1^{75}) and (0^{4819}1^{43}).  Direct intersection with the
componentwise forced-colour set gives the same 75 and 43 values.  Finally, the
two independently emitted minimizing tables have the common SHA-256
`8c56e7786e7bb5979aa447d0b314f036e7c18e18e7df07b4534e3f9a9fcde90b`.
∎

### Essential limitation

Changing a cut pattern changes the pieces, their boundary run ages, and every
rank-10--17 crossing-provider catalogue.  Thus Theorem 3.1 does **not** say
that the selected cutting has 75 robust-zero or 43 extendable-zero colours.
It says only that, measured against the old canonical lists, all avoidable
cost can be removed.  The provider catalogue must be regenerated after the
choice.

## 4. Exact patterned seam-flow theorem

Fix one pattern (P_i\in{\cal P}_i) for each component, and write
({\cal B}(P)) for the resulting 6,281 pieces.  A state of an oriented piece
contains:

1. its first and last three owner words (or the entire piece when shorter),
   for maximal depth-3 replay;
2. for every coordinate, its endpoint bit and its prefix/suffix positive-run
   age, capped at four, together with the flag saying that the current run is
   the globally clipped initial run;
3. its complete prefix-, suffix-, and internal interval-OR decks.

When an oriented piece is appended, a deterministic transition does the
following.

* It checks Johnson adjacency at the seam.
* Using the retained owner suffix, it constructs every newly determined cell of
  the maximal depth-3 source, requires it to be nonzero, and checks every newly
  determined depth-3 owner replay equation.
* It updates the capped positive-run automaton.  A (1\to0) transition is
  accepted only if the completed run has length at least four, except at the
  global initial boundary; the final positive run may be clipped at the global
  terminal boundary.
* It emits every newly completed crossing interval union.  This is computed
  exactly by adjoining the piece prefix deck to the current suffix-OR deck;
  the latter is a chain of at most 18 distinct masks.
* After the last piece, the accepting transition performs the three trailing
  maximal-source boundary steps and verifies the final three owner replay
  equations.  Only then may the terminal positive run be treated as clipped.

Let (U(P)) be the set of the 1,419 upper q1 edge colours deleted by the
chosen cuts.  For (r=11,\ldots,17), define the pattern-dependent internal
hole bank

\[
 H_r(P)=\binom{[17]}r\setminus
 \{O_a\cup\cdots\cup O_b:\text{the whole interval lies in one piece}\}.
\]

For q1 lower colours, put

\[
 L(P)=\binom{[17]}8\setminus
 \{O_j\cap O_{j+1}:\text{the edge survives inside one piece}\}.
\]

Then (|L(P)|=6,281) for every minimum pattern choice.

### Theorem 4.1 (necessary and sufficient finite-state completion)

For a fixed minimum-pattern choice (P), an ordering and orientation of its
pieces gives a positive-run-safe, maximal-source-replayable owner path with
complete upper ranks 10--17 if and only if there is an accepting path in the
transition system above which

1. uses every physical piece exactly once;
2. has seam unions covering every colour in (U(P));
3. emits every target in (H_r(P)), for every (r=11,\ldots,17).

For such a path, its exact number of uncovered lower q1 colours is

\[
  |L(P)|-
  \left|L(P)\cap
    \{O_{\rm end}(B_j)\cap O_{\rm start}(B_{j+1}):1\le j<6281\}
  \right|.
\tag{4.1}
\]

In particular it is at most 6,281, independently of the seam choices.

#### Proof

The pieces partition all owners and retain every internal owner adjacency.
The last-three-owner state is sufficient for every depth-3 erosion/replay
equation that becomes determined on appending a piece.  For arbitrary-width
upper witnesses, all suffix unions of a fixed word form an inclusion chain;
there are at most 18 distinct values on a 17-set.  On appending a new owner,
OR it with every member of the old suffix deck (and include the singleton
owner) to obtain both every newly ending interval and the new suffix deck.
Thus the deck update loses no long interval witness.  The capped run state
accepts exactly when no completed internal positive run has length below four.
Hence the transition tests are both necessary and sufficient for the stated
chronology conditions.

All upper witnesses wholly internal to pieces are already present; every other
upper witness is emitted by a crossing transition, possibly across several
short pieces.  Rank 10 is separately required on literal seams because it is
the physical upper q1 palette.  This proves the upper equivalence.

The surviving internal lower edge colours are pairwise distinct.  Their
complement is exactly (L(P)).  A new seam removes a member of this missing
bank precisely when its intersection colour belongs to (L(P)), and repeated
seam colours count only once.  This gives (4.1). ∎

### Corollary 4.2 (q1 lower slack is not the immediate obstruction)

Since (6,281<7,401), the rank-8 omission budget is automatically respected
before accounting for deeper/common-source compiler damage.  The raw margin is
(7,401-6,281=1,120), and useful seam intersections only improve it.

This corollary is q1-only.  It does not assert a common maximal source, the
generalized lower compiler, or common-Q feasibility at deeper ranks.

## 5. Audit of immediate obstructions

The canonical pairwise raw endpoint graph has at least one rank-10 provider
for each of its 1,419 destroyed colours (`raw zero=0`).  Therefore none of the
132 forced cut colours is excluded by owner-pair geometry alone.  There is no
forced-colour obstruction at that weakest level.

At the stronger canonical tests there are 75 forced colours in the robust-zero
set and 43 in the extendable-zero set.  Neither is a global impossibility:

* robust pairwise testing discards legal stateful extensions through
  constant-one pieces;
* both tests use the canonical fragmentation, while a new pattern changes the
  boundary states and provider arcs;
* ranks 11--15 require multi-seam windows, not merely pairwise seams.

No Hall obstruction for the full patterned transition system is proved here.
The exact next finite step is therefore:

1. choose the common 75/43-minimizing cut table as a seed;
2. regenerate its q1 cut bank and ranks 11--17 full interval-OR hole banks and
   stateful transition
   catalogue from scratch;
3. separate zero-support targets and resource cuts in the suffix-deck/source
   transition system;
4. only after an accepting owner braid is found, solve the common-source and
   generalized lower-compiler rows within the remaining 1,120 q1 margin.

## 6. Artifacts and hashes

Authenticated source forest:

* `scratch/h2_k17_m9_multicomponent_20260801/phase_m9.selected.tsv`, SHA-256
  `49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de`;
* `scratch/threadA_k17_m9_scd_lower_compiler_20260801/components.tsv`, SHA-256
  `dc4557fb557dccb87bec15476e11b81655d17c6c6c5295b020fec95adbcb47ef`.

Audited enumerator:

* `scratch/audit_k17_m9_min_cut_options_20260801.cpp`, SHA-256
  `fec8f143d92525e77d64836a46b1b10d2ddaceea67f9843c79425977e469a06d`.

Independent audit:

* `scratch/threadA_k17_m9_cutflex_audit_20260801/independent_cut_option_audit.py`,
  SHA-256 `24fa6eb15d878e9b80c31a8a8e64d9bcdc64d252e8c5e83ffc9850e845d417e4`;
* `scratch/threadA_k17_m9_cutflex_audit_20260801/independent.audit.json`,
  SHA-256 `91da38c0d597d9cf08eb09ad5d2c4057eacf149236d5909bd8c3d8d8bcc7aa80`,
  canonical payload SHA-256
  `d233f28704d63e9a415bcc4cb31cbe20038485b76822a43959914dbf1d7a5cac`.

Reference-set hashes:

* robust zero list:
  `5c5dede719b749763a3a571ae610ea91f801fef1b749ce386367a2f9912333e2`;
* extendable zero list:
  `12b69ab269e07df1194be58cbd662f9ba9ca852cd673fe204d89f1e682d7cc25`.

One implementation detail matters when comparing arc totals: the rank-10
replay program represents both orientations even for singleton pieces.  This
duplicates some physical arc occurrences, but it cannot change any zero-provider
set.  The 75/43 and 132/4,232 conclusions are independent of those arc
multiplicities.
