# The `k=17`, `m=9` minimum-cut obstruction, eight-facet rails, and the compound-fragmentation gate

Date: 2026-08-01  
Lane: A / SCD cut flexibility / resident facet rails  
Status: theorem plus independently replayed finite audits.  The minimum-cut
face is rigorously excluded.  A fixed 152-extra-cut rail face has an exact
lower-palette optimum but still fails rank-ten provider support.  A newer
authenticated 30-compact-socket bank supersedes that rail face as the best
finite construction and fits the compound-fragmentation theorem below.
No owner braid, common source, compiler, or `k=17` word is claimed.

## 1. Frozen setting

The authenticated SCD owner forest has

\[
  |\mathcal O|=\binom{17}{9}=24310,
  \qquad c=4862,
  \qquad |E|=19448.
\]

Its components are directed Johnson paths.  Their old rank-ten union
colours are all distinct and cover `binom([17],10)` exactly.  Their old
rank-eight intersection colours are also distinct, so they cover 19448 of
the 24310 rank-eight masks and leave 4862 masks for the lower compiler.

Depth-three positive-run factorability requires cutting every internal
positive run of length at most three.  The interval-stabbing theorem gives
exactly 1419 minimum cuts and hence

\[
                         P_0=4862+1419=6281             \tag{1.1}
\]

pieces.  Over all components there are 8894 minimum cut patterns.

The base piece file is

`scratch/h2_k17_m9_multicomponent_20260801/h2_residence_pieces.json`,

SHA-256
`9889b94b7d18078986965b5b78290b87b2ce8dde78bfe78b03ac3d9c5ad69f88`.

## 2. Rank ten is an exact seam-local obstruction

### Theorem 2.1 (rank-ten seam necessity)

Let

\[
                         A_0,A_1,\ldots,A_t             \tag{2.1}
\]

be a contiguous interval in a chronology of distinct rank-nine owners,
with every adjacent pair a Johnson edge.  If

\[
                         \bigcup_{i=0}^t A_i=U,
                         \qquad |U|=10,                 \tag{2.2}
\]

then `t>=1` and every adjacent union is `U`:

\[
                         A_i\cup A_{i+1}=U.             \tag{2.3}
\]

Consequently, if the unique old edge of colour `U` was cut, every new
witness for `U` contains either an external seam of colour `U` or an
internal edge of a newly planted block of colour `U`.

#### Proof

A single owner has rank nine, so `t>=1`.  Every `A_i` is contained in `U`.
Two distinct adjacent rank-nine sets in the Johnson graph have union of
rank ten.  Thus `A_i union A_(i+1)` is a rank-ten subset of the rank-ten set
`U`, proving (2.3).  If the interval used only retained old adjacencies,
one of them would be the unique old `U` edge, contrary to the
assumption that it was cut.  `square`

This argument is special to rank ten.  A rank-eleven or deeper target may
require more than the two seam-endpoint owners (and may span several seams),
so an endpoint-pair or truncated prefix/suffix-deck zero at those ranks is
not automatically an arbitrary-width no-go.

### Corollary 2.2 (the complete minimum-cut face is impossible)

In the union of every oriented segment from every minimum cut pattern,
there are 243 possible cut colours with no extendable one-seam provider at
all.  Separately, the option-conditioned audit finds fourteen original
components having no minimum pattern whose cuts are all individually
supported; the sum of their independent minimum unsupported counts is
fourteen.  (Thirteen of these are forced by the global 243-colour set; the
fourteenth is an option-specific incompatibility.)  Since old rank-ten edge
colours are globally distinct, every global 1419-cut choice contains at
least fourteen distinct unsupported selected colours in the full
option-conditioned relaxation.

Therefore no ordering and orientation of the unchanged minimum fragments
can be upper-q1 complete.  This remains true with arbitrary topology and
with arbitrarily many seams: Theorem 2.1 forces a seam of the missing
colour, while the extendable seam predicate is a necessary relaxation of
any genuinely resident seam.

The fourteen masks in

`scratch/k17_m9_extendable_independent_residual14_20260801.txt`, SHA
`dca7f8bd114ef9e86191272a43e148f476a85a45c57e0c627db98c525b09011a`,

are one independently minimizing representative, not a set forced in every
minimum fragmentation.  The exact coupled support relaxation is stronger:
its optimum is nineteen omissions (`b18` is DRAT-UNSAT and `b19` is SAT).
That nineteen is still only a pairwise-support optimum, not a chronology.

## 3. Exact resident facet-rail algebra

Let `U` have rank `r+1`, let `t>=2`, and choose distinct labels

\[
                         u_0,\ldots,u_{t-1}\in U
\]

and put `F_j=U-u_j`.

### Theorem 3.1 (ordered facet rail)

The owner sequence

\[
                         F_0,F_1,\ldots,F_{t-1}         \tag{3.1}
\]

has the following exact signature.

1. It is a simple Johnson path.
2. Every internal upper-q1 colour is `U`.
3. Its lower-q1 colours
   \[
                    U-\{u_j,u_{j+1}\},\qquad0\le j<t-1 \tag{3.2}
   \]
   are pairwise distinct.
4. Every internal interval of at least two owners has union `U`; hence
   \[
        \operatorname{Pref}(F)=\{F_0,U\},\qquad
        \operatorname{Suff}(F)=\{F_{t-1},U\},\qquad
        \operatorname{OR}(F)=U.                        \tag{3.3}
   \]
5. The owner trace of `u_j` is
   \[
                         1^j0,1^{t-1-j}.               \tag{3.4}
   \]
   An unselected coordinate of `U` has trace `1^t`, and a coordinate
   outside `U` has trace `0^t`.

For residence depth `h`, assume `t>=h+1`.  Let `ell(x)` be the incoming
positive suffix age and `rho(x)` the outgoing positive prefix age.  The
rail with both exterior contexts present is positive-run resident exactly
when the following exterior conditions hold, in addition to residence
inside its neighboring pieces:

\[
\begin{array}{ll}
1\le j\le h:
  &\ell(u_j)\ge h+1-j,\\[1mm]
t-1-h\le j\le t-2:
  &\rho(u_j)\ge h-t+j+2,
\end{array}                                             \tag{3.5}
\]

`ell(u_0)` and `rho(u_(t-1))` must each lie in
`{0} union [h+1,infinity)`, and both exterior ages of every coordinate
outside `U` must lie in that same clean set.  If the rail lies at the unique
global initial or terminal boundary, drop the requirements on the clipped
side; no internal component boundary receives this exception.

#### Proof

Distinct facets differ precisely in their two omitted labels, which proves
the Johnson, union, and intersection assertions.  Distinct consecutive
unordered label pairs give distinct values in (3.2).  Any interval of at
least two facets contains two different omissions and therefore already
has union `U`, proving (3.3).  Formula (3.4) is immediate.  Its left
positive piece has length `j` and its right piece length `t-1-j`.  A
nonempty piece shorter than `h+1` needs exactly the complementary exterior
age in (3.5).  The endpoint zero terminates the corresponding exterior
run, and a coordinate outside `U` sees zero throughout the block; those
runs must therefore be clean separately.  These cases exhaust all
coordinates.  `square`

### Corollary 3.2 (the depth-three eight-role Hall test)

For `h=3,t=8`, the omitted labels must occupy the roles

\[
 \text{L-clean},\quad L\ge3,\quad L\ge2,\quad L\ge1,
 \quad R\ge1,\quad R\ge2,\quad R\ge3,\quad\text{R-clean}. \tag{3.6}
\]

For fixed oriented exterior pieces, a rail order exists if and only if the
bipartite graph from the eight omitted labels to these eight roles has a
perfect matching, where the first and last roles additionally require the
corresponding exterior Johnson adjacency.  Cleanliness for coordinates
outside `U` is a separate common prerequisite.

Indeed, an order is precisely a bijection from labels to roles, and
Theorem 3.1 lists every constraint attached to a role.  Thus (3.6) is an
ordinary eight-by-eight Hall test.  It is not automatic from singleton
extraction.

No separate nonzero-aperture obstruction occurs: four consecutive
rank-nine owners have intersection of rank at least six.  This does not
imply the later common-Q/compiler conditions.

## 4. Exact extraction cost on the representative fourteen

The socket catalogue

`scratch/k17_m9_extendable_residual14_facet_sockets_20260801.tsv`, SHA
`36e637d41631ba728f672b8556cf332ac650b32ad1c36a591b729039603f0e4f`,

contains all ten physical facets of each representative target.

### 4.1 The proposed ten-facet bank

The 140 facet owners are pairwise distinct.  Isolating all of them into
their maximal pure blocks forces 220 distinct boundaries.  Completing the
positive-run interval stabbing problem then gives exactly

\[
                         K_{10}=1613,qquad P_{10}=6475, \tag{4.1}
\]

so its raw lower-hole count is 6475 and its remaining scalar reserve is
`7401-6475=926`.  Its post-cut upper-hole counts in ranks 10 through 15 are

\[
                         1613,2595,1728,640,133,18.     \tag{4.2}
\]

In this particular extraction the old `U` witness remains inside one of
the nine retained pure facet blocks for every representative target.
Accordingly, the full ten-facet macro repairs none of the fourteen: they
were already covered after extraction.  The full bank is therefore
strictly more expensive than needed for this face.

### 4.2 Eight internally self-buffering, exterior-conditional facets

Select the fixed eight facets recorded in the socket table and isolate
each as a singleton atom.  The 112 owners and their 178 required boundaries
are pairwise distinct.  The exact minimum positive-run completion is

\[
                         K_8=1571,qquad P_8=6433.       \tag{4.3}
\]

Thus the architecture costs 152 cuts beyond the 1419-cut minimum face and
has raw lower-hole count 6433, leaving 968 scalar units.  Before adding the
rail edges, the upper-hole counts in ranks 10 through 15 are

\[
                         1571,2556,1708,630,128,16.     \tag{4.4}
\]

All fourteen representative targets occur among the 1571 rank-ten holes.
Ordering each selected facet set as a rail adds seven internal copies of
its target and therefore repairs those fourteen rank-ten demands locally.
It does not repair the other casualties in (4.4).

The 178 boundaries and the value 1571 are conditional on this chosen
singleton-isolation architecture.  They are not lower bounds for every
possible facet embedding.

## 5. Exact lower-palette optimum of the fourteen rails

Let `R` be the 17877 lower colours on original edges retained by the
1571-cut bank.  For each target `U`, give an edge between two selected
facets the cost one when their intersection belongs to `R`, and cost zero
otherwise.  An eight-facet order is a Hamilton path in this weighted
complete graph.

### Theorem 5.1 (seven is the exact retained-collision minimum)

The sum of the fourteen independent minimum Hamilton-path costs is seven.
There are fourteen path orders attaining those minima simultaneously whose
98 lower colours are globally distinct.  Their ledger is

\[
\begin{array}{c|c}
\text{rail lower colours} & 98\\
\text{collisions with retained old colours} & 7\\
\text{hits on colours deleted by the 1571 cuts} & 80\\
\text{hits on the 4862 pre-existing lower holes} & 11.
\end{array}                                             \tag{5.1}
\]

Consequently the rails fill exactly 91 raw lower holes, leaving

\[
                         6433-91=6342                 \tag{5.2}
\]

and scalar reserve `7401-6342=1059`.

#### Proof

For one selected eight-facet set, let

\[
 D(S,j)=\min\{\text{cost of a path through }S
                 \text{ ending at }j\}.
\]

The exact Held--Karp recurrence is

\[
 D(S,j)=\min_{i\in S-\{j\}}
       \bigl(D(S-\{j\},i)+{\bf1}_{F_i\cap F_j\in R}\bigr), \tag{5.3}
\]

with singleton base value zero.  The independently implemented subset DP
gives per-target minima

\[
\begin{array}{c|rrrrrrrrrrrrrr}
U&12250&15070&19709&24371&31988&32286&40870&45903&57583&59815&75693&79722&8165&86735\\
\hline
\min&3&0&1&0&0&0&0&0&0&0&1&1&1&0.
\end{array}                                             \tag{5.4}

Their sum is seven, a lower bound even before cross-rail distinctness.
Literal replay of the emitted orders verifies all 98 intersections,
global distinctness, and equality in (5.4).  This attains the lower bound.
The counts in (5.1)--(5.2) then follow by partitioning the 98 colours into
retained, deleted-old, and pre-existing-hole classes.  `square`

This theorem closes scalar lower-q1 capacity only.  Seven retained-palette
collisions and the exact addresses of the 91 gains still matter to common-Q.
The minimizing orders in Theorem 5.1 do not impose the exterior role-Hall
conditions (3.6); simultaneous residence-compatible ordering remains part
of the later chronology problem.

## 6. Regeneration fails on the two frozen 1571-cut banks

The complete seam-catalogue generator was run from source SHA
`683d57daab40e28b41a5f0328d216f5a71082f21247d134fc54cd4e16336dcea`
and binary SHA
`a38f9385947cdeb279d60c2b72f6f2371e6eb1af44841218d5efb44152add7e5`.
The frozen parent inputs had hashes

\[
\begin{array}{c|c}
\text{phase map}&381dc1068aa39403d442c3d3b2d45a1c334dbc1e2b206449d5f678a6c1b6d473\\
\text{winner model}&75946e58bea2147d3899eae3f0f99aca9ba4ea413682c938ca59534b980a687c.
\end{array}
\]

For the initial eight-facet completion, the generator reports

\[
 \operatorname{zero}_{\rm stateful}(10)=279,
 \qquad \operatorname{zero}_{\rm stateful}(11)=11.       \tag{6.1}
\]

None of the representative fourteen lies in the rank-ten zero bank, so the
facet extraction has genuinely made local providers for all fourteen.
Nevertheless, Theorem 2.1 makes each of the 279 new rank-ten zeros a valid
fixed-bank obstruction.

Next freeze the 178 extraction boundaries and enumerate every minimum
additional interval-stabbing completion.  There are 8909 alternatives in
the sum over components.  Minimizing, independently and exactly, the
number of cuts lying in the previous 279-mask zero bank still selects 32
such cuts.  The resulting cut table has SHA
`cf8a68faca78eef35228c856b85fd28cdfd7774a0912f47f2e2da85c071be3f8`.
After regenerating the complete catalogue, its exact result is

\[
 \operatorname{zero}_{\rm stateful}(10)=289,
 \qquad \operatorname{zero}_{\rm stateful}(11)=14.       \tag{6.2}
\]

Thus the one-bank best response rotates rather than contracts the rank-ten
casualties.  The 32 is an exact optimum against the previous bank, not a
joint lower bound.  The rank-eleven values in (6.1)--(6.2) are diagnostics
only: the generator truncates each prefix and suffix deck at seven owners,
so they are not arbitrary-width no-go counts.

The rank-ten zeros are sound despite the generator not explicitly testing
Johnson distance.  If two rank-nine endpoint owners have rank-ten union
`U`, they are automatically distinct facets of `U` and hence a Johnson
pair.  Moreover, the generator's extendability test is weaker than full
run-age realizability.  A zero in that superset therefore remains a no-go.

## 7. The current `b19` socket branch is not a physical master

The authenticated all-minimum `b19` model is an exact support relaxation:
it selects 4862 patterns, one per component, from 8894 available patterns,
and nineteen omitted rank-ten colours.  Its verified model contains 4773
positive arc variables and no socket variables.  Mode 1 imposes neither
endpoint degree nor colour capacity, and it has no connectivity or common
run-age chronology.

The optional socket branch in
`scratch/build_k17_allmin_support_closure_cnf_20260801.cpp` must not be used
as a physical certificate in its current form:

1. the named eight-facet TSV has ten fields and is rejected outright;
   separately, the eighteen-field loader retains only `L=3` `PASS` rows;
2. it imports only a scalar extra-cut count and child colours, not the exact
   extraction-boundary identities or refined local configurations;
3. it never removes extracted facets from their base segments or constructs
   a replacement owner partition, so a naive materialization would
   duplicate owners;
4. it does not construct the refined residual pieces or replay the rail;
5. it has no exact in/out equations, subtour cuts, full run automaton,
   ranks 11+, or common-Q row.

The nineteen socket rows were optimized individually and are not jointly
selectable: owner `41199` is shared by targets `41215,57583`, owner `70366`
by `70398,72414`, and component `2276` is assigned incompatible options
zero and three by `40870,59815`.  Therefore no heavy solve of this
physically incomplete optional branch was launched.  The present
builder/verifier also postdate the frozen `b19` formula and are not claimed
as its source lineage.

## 8. Exact compound-fragmentation completion theorem

Let each original component `c` have a finite catalogue `K_c` of complete
local configurations.  A configuration records all ordinary residence
cuts and all socket extraction cuts and partitions every original owner
exactly once into exposed atomic path pieces.  A certified macro column `M`
has an owner-disjoint required atom set `Req(M)`, an exact ordered Johnson
owner word using precisely the owners of those atoms, and its literal endpoint,
internal upper/lower colours, run summary, prefix/suffix OR decks, and
maximal-source replay.  Selecting `M` consumes every atom in `Req(M)` and
replaces them by that one ordered block; unconsumed atoms remain ordinary
blocks.  The eight-facet rail is one macro type.  A separately replayed
guard--three-facet--guard socket, such as those in the authenticated
30-socket bank, is another; it is not inferred from Theorem 3.1.

### Theorem 8.1 (necessary and sufficient finite master)

Within any such finite configuration/macro catalogue, a depth-three
maximal-source-valid, positive-run-resident linear Hamilton owner path with
complete upper interval deck and at most 7401 missing lower-q1 colours
exists if and only if there are integral variables satisfying all of the
following.

1. Exactly one configuration is chosen for every original component.
2. Let `y_(c,kappa)` choose the local configurations, define the exposure
   indicator exactly by
   \[
      a_s=\sum_{\kappa\in\mathcal K_c:\,
                s\in\operatorname{Atoms}(\kappa)}y_{c\kappa},             \tag{8.0a}
   \]
   for an atom `s` of component `c`, and let `z_M` select macro `M`.  Then
   \[
       z_M\le a_s\quad(s\in\operatorname{Req}(M)),
       \qquad
       \sum_{M:s\in\operatorname{Req}(M)}z_M\le a_s.   \tag{8.0}
   \]
   Atom `s` remains an ordinary active block with indicator
   \[
                  a_s-\sum_{M:s\in\operatorname{Req}(M)}z_M.
   \]
   Thus the selected macros together with all unconsumed atoms partition
   all 24310 owners exactly once.
3. Every active block has one orientation.  A successor variable exists
   only when the last owner of its oriented left block and the first owner
   of its oriented right block form a Johnson edge.  Exact predecessor and
   successor equations, with one boundary dummy, form a path/cycle cover.
   The dummy has degree one on each side and marks the unique global reset;
   every proper active-block set satisfies the usual subtour inequality.
   Removing the dummy therefore leaves one Hamilton path.
4. Starting at the block after the dummy, the ordered block scan is accepted
   by the exact boundary automaton.  Its state contains the last three
   owners, every coordinate's terminal bit and capped positive-run age, the
   initial-clipping flags, and the complete distinct suffix-OR deck.  It
   checks delayed maximal-source replay and every newly completed internal
   run.  At the block before the dummy it flushes the last three delayed
   source equations, checks every terminal source cell is nonzero, and
   permits clipping only at this one global initial/final boundary.  There
   is no physical seam across the dummy.
5. If the unique old edge of rank-ten colour `U` is cut, then either a
   selected external successor seam has union `U` or the internal q1 deck
   of a selected macro contains `U`.
6. On appending a block `B`, every crossing interval value is generated by
   \[
       \{S\cup P:S\in\operatorname{SuffDeck}_{\rm old},
                    P\in\operatorname{Pref}(B)\},       \tag{8.1}
   \]
   and the suffix deck updates to
   \[
       \operatorname{Suff}(B)\cup
       \{S\cup\operatorname{OR}(B):
                    S\in\operatorname{SuffDeck}_{\rm old}\}. \tag{8.2}
   \]
   The internal and emitted values cover every target of ranks 10 through
   17.
7. The union of retained old lower colours, external seam intersections,
   and every selected macro's internal lower intersections misses at most
   7401 rank-eight masks.

#### Proof

A physical chronology selects its local fragmentations, macro blocks,
orientations, and successor edges, giving items 1--3.  Literal source and
run replay gives item 4.  Theorem 2.1 gives item 5.  Splitting a crossing
interval at the appended block proves (8.1).  A suffix interval ending at
the last owner of the new block either lies wholly in `B` or is an old
suffix followed by all of `B`, which proves (8.2).  This establishes item 6
by induction.
Item 7 is the literal lower-colour ledger.

Conversely, items 1--3 give one owner order with no duplication.  Automaton
acceptance gives a valid depth-three source chronology and positive-run
residence.  The same induction on (8.1)--(8.2) gives the exact upper deck,
and item 7 gives the stated lower omission bound.  `square`

Once configurations, macros, and orientations are frozen, anonymous
successor assignment is a bipartite matching and has the ordinary Hall
criterion.  Configuration selection, coloured service, subtour avoidance,
run state, and upper-deck state are not one Hall problem.  They are the
precise integral correlations that the current support master omits.

## 9. Sharp remaining gate and adversarial audit

The proved boundary is now:

* the unchanged 1419-cut face is impossible at rank ten;
* a concrete 152-extra-cut bank exposes 14 disjoint candidate rails that
  are internally self-buffering but exterior-conditional;
* its lower-q1 ordering has exact collision optimum seven and ample scalar
  reserve;
* the rails service the chosen fourteen masks, but the regenerated fixed
  bank still has 279 rank-ten no-provider colours (289 after one exact
  best-response reweight).

This fixed eight-facet face has now been superseded as a construction by
the independently authenticated compact-socket bank in
`MATH_THEOREM_K17_SCD_COMPACT_SOCKET_BANK_AND_UPPER_CASUALTY_LEDGER_20260801.md`.
It uses thirty guarded three-facet sockets, ninety distinct facet owners,
sixty disjoint exposed guard intervals, and 81 genuinely extra cuts.  Its
topology-relaxed, individually projected unsupported-child list is empty:
three children are self-served, 77 have individual extendable seam
providers, and the last child `97508` is serviced by the thirtieth socket.
No common capacity-one provider selection is asserted.  Starting from
6362 raw fragments, the construction coalesces eighty extracted facet
chunks and sixty guard pieces into thirty socket paths,

\[
                         6362-80-60+30=6252.             \tag{9.0}
\]

The result is a literal path forest whose 6252 pieces are internally
positive-run-clean, with component boundaries clipped; it contains every
owner exactly once.  Relative to its frozen 6281-piece base, the
newly-lost/newly-gained upper counts at ranks 10 through 15 are

\[
       127/88,\quad97/66,\quad49/42,\quad21/21,
       \quad7/8,\quad0/1.                              \tag{9.1}
\]

Its resulting internal upper holes are

\[
                         1458,2429,1583,549,101,10      \tag{9.2}
\]

at ranks 10 through 15 and zero at ranks 16 and 17.  No regenerated final-
bank seam census shows that all 1458 rank-ten holes are simultaneously
serviceable.  The sharp live finite lemma is therefore the remaining part
of Theorem 8.1 on this 6252-piece/path-block bank: regenerate and solve a
common capacity-one successor/macro-hyperarc system that covers (9.2),
satisfies the global run automaton and connected topology, and then passes
the literal lower common-Q compiler.  Common-Q is an additional gate beyond
Theorem 8.1's scalar lower-q1 conclusion.

The eight-facet audit remains useful for two reasons.  It proves that a
one-bank zero-price iteration is not an absorber, and it supplies an exact
rank-ten separation theorem for any future chronology master.  It should
not be preferred over the 30-socket bank as a construction.

The following overclaims are explicitly excluded.

1. The representative fourteen are not universal forced masks.
2. Positive-run factorability is not two-sided signed residence; every
   selected omitted label has a singleton zero in its rail trace.
3. Eight facets suffice only after the exterior role-Hall and outside-`U`
   cleanliness tests.
4. Scalar lower slack does not imply a common compiler.
5. A rank-eleven pairwise or seven-owner-deck zero is not a full
   arbitrary-width obstruction.
6. Absence of rank-ten zero providers would still not prove simultaneous
   tail/head/orientation capacity or connectivity.
7. The 30-socket bank closes its colourwise unsupported-child list, not a
   simultaneous provider matching, the global arbitrary-width deck, or the
   common compiler.

## 10. Reproducibility

Principal artifacts:

* eight-facet extraction driver
  `scratch/threadA_k17_m9_cutflex_ext_20260801/audit_residual14_eight_facet_macro.py`,
  SHA `eb1ab5363da06cc1ad6b613cb38130488c1c79753a2e335c46b6c00fd5535183`;
* extraction audit JSON, SHA
  `a83d68a8b1063071d40396b20fcf7fd6b5723108ba98ff295a293b522cddb5a6`,
  payload `9e932ba94f319ff969f9cbd797bd8c4b67602dc03862899354d6b9ad03992b89`;
* exact conditioned reweight driver, SHA
  `53cf4b3c2f0d76ed16cb362747d321f899118f557f35e087af6d00022e3f860f`;
* conditioned reweight audit JSON, SHA
  `e180530a1bf992616de78649ad02f18ae2b3ddd066a432f729f0bcf7921b619a`,
  payload `d5095a664bd3fbb424b8d62724c59ca96e93f552f1c44d1cf94ee633cfa3c3db`;
* regenerated census stdout, SHA
  `b03447e41773d2c22a0d5483d6110baf6df7eaf324dc21ae63f9e30051b2f8a5`;
* lower-path constructor, SHA
  `cd1482d31947eb226a03c01f5a9bcd5441984e8204f83e4c789b36db807d5ff8`;
* emitted lower paths, SHA
  `938e8109e498117ba62d5099f27860405ddfb1224387e6fc07267070070e976f`;
* independent Held--Karp audit, SHA
  `c435ba8d8bc4916468d27dd43a375254db9f928f81006446fe0baad3e1eafd12`,
  payload `b104bd23d9b3898eb3abda31d286d5877a2adeabbb1654f23386f469686dd7b8`.

Authoritative compact-bank comparison:

* theorem SHA
  `50999ccc4329d7beb404559e18412845dcba64006bc55eecf3b94fd27d21d657`;
* bank TSV SHA
  `14e444919ef4daf6aeee1639cbe1632299193cbd8a40838c0cb652d123018697`;
* primary and independent audit SHAs
  `19ab65a1a0e946486a81ca0ccc8dd46e1a06187b1b977e414461090e30195c07`
  and
  `d77531b5ad73e3631b2df739febc725635ccd96656710c4de8df587d8cba6aa7`;
* upper-casualty audit SHA
  `2cdfc7aa7c275f70332d0ed3b7a77077d241ffefbf29c73f20b74c1b859cfc30`.

The enumeration and seam regeneration ran on H100 CPU under explicit
`prlimit` memory/CPU caps in
`/home/amodo/or15/work/threadA_k17_m9_cutflex_ext_20260801`.  No local heavy
search was run.
