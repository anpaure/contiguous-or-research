# A finite parent bank supplies a second genuine GOOD-sector fusion

2026-09-08. Status: exact finite construction, preceded by an exhaustive
topology check of one analytically specified 221-parent family. All
mathematical execution was on h100. This records the completed 849-owner
stage; it is not an optimal k17 word or an all-dimensional equality proof.

## 1. Result and actual state

Starting from the verified 475-owner stage, the chosen clean C6 merges

    giant_475 + old_6(187) + old_7(187) -> one 849-cycle.

The two fresh original components have peak-pruning profile
(3,1,1,1,1,1), corresponding to soliton partition (6,1,1). Every owner
is retained once. The operation has the following fully checked properties:

* exact equality of the complete affected proper upper support, with no
  local loss and no local gain;
* preservation of all 41,225 global proper upper targets against the
  actual current 306-owner linear prefix and remaining cycles;
* exact preservation of the rank-eight adjacent-intersection multiset;
* minimum positive coordinate run six on the new cycle;
* no changed owner or edge in the 306-owner prefix; and
* an actual nonempty 849-letter cyclic depth-three source, minimum letter
  rank six, replaying every width-four owner and width-three facet.

There are now 136 GOOD cycles together with the unchanged 306-owner path.
The surviving mountain_103 component was not altered. In particular the
existing backup there for target 131062 remains valid. The present fusion
does not rely on outside backups to replace a local upper loss, because
its complete local support is equal before and after.

The global rank-eight palette still has the same two holes 43857,46420 and
one duplicate inherited from the 306-prefix stage: both subsequent C6
operations have preserved its entire counter.

## 2. Why the candidate family has exactly 221 parents

Consider rank-seven deficit-three parents H on the 17-cycle. At their
three forward-unmatched zeros, write their rooted word as

    0 D_0 0 D_1 0 D_2,

with total Dyck semilength seven and soliton profile (6,1). Such a triple
has one of two forms.

1. Both solitons lie in one block. That block is one of the eleven
   semilength-seven shapes

       A_j=1^6 0^j 1 0^(7-j), 1<=j<=6,
       B_j=1^j 0 1^(7-j) 0^6, 1<=j<=5.

   It can occupy any of the three blocks, giving 33 triples.
2. The mountain 1^6 0^6 and the isolated peak 10 occupy distinct blocks.
   There are six choices of their ordered block positions.

The list is exhaustive: the total peak-pruning profile has two initial
peaks, after whose deletion only the single mountain remains. In a
two-peak Dyck word this forces either the internal descent or internal
ascent to have length one, yielding precisely the A/B list. If the peaks
are in different blocks, each block is a mountain, of sizes six and one.

Thus there are 39 rooted block descriptions. Taking their 17 physical
rotations gives 663 descriptions. Each physical parent is represented
at exactly its three unmatched zeros, so there are 221 distinct parents.
The finite checker independently verified the deduplication and exact
threefold multiplicity.

This is the complete stated (6,1)-parent family, not an enumeration of all
possible clean C6s in the factor.

## 3. Exact filters against the 475-stage graph

For every parent H and its cyclically ordered unmatched zeros a_i, the
checker evaluates the actual original inverse PBBS map at H+a_i. Their
omitted reverse labels must agree at one pivot c. It then puts

    K=[17] minus (H union {a_0,a_1,a_2,c}),
    P_i=K+{a_i,a_(i+1)}, Q_i=K+{a_i,c}.

The three old P_i--Q_i edges are tested in the **current** graph after the
mountain and 475 surgeries. For each P_i, the remaining current neighbor
must delete the same one coordinate of K, giving the actual common
companion-deletion condition. Finally the three old edges must occupy
three distinct GOOD components and at least one must lie in giant_475.

The exact nested counts are:

| condition | parents retained |
|---|---:|
| explicit family | 221 |
| common reverse pivot | 221 |
| all old shore edges currently present | 217 |
| common current companion deletion | 217 |
| touches giant_475 | 145 |
| touches three distinct GOOD components | 88 |
| the other two components both have profile (6,1,1) | 72 |

All 72 last-stage candidates were generated before any upper-support or
residence audit. The deterministic selection is the least numerical
parent H among them. Only this one selected move received the full
upper/residence audit in the completed run.

## 4. Selected move

The selected parent is H=223. One rooted description is

    (D_0,D_1,D_2)=(11111011000000,empty,empty), rotation16.

Its arms are (16,14,15), common pivot is coordinate8, core mask is15904,
and the unchanged companion deletes coordinate9 at all three P endpoints.

Delete the lower-owner edges

    (97824,81696), (65056,32544), (114208,48928),

and insert

    (97824,32544), (65056,48928), (114208,81696).

The current affected components have lengths 475,187,187. Degree-two
traversal after the edge replacement gives one literal 849-cycle. The
old and new affected rank-eight palette counters are equal.

The new positive-run histogram is

    6:2, 7:596, 8:108, 9:15, 16:33, 18:67, 19:2,
    20:3, 21:4, 22:1, 23:1, 29:15, 30:1, 32:1.

No positive run has length below four. Proper upper targets were
enumerated at every cyclic start until the full 17-set appeared. The
complete old and new support sets are identical. The JSON contains every
target's literal old/new occurrence, not only a rank census.

## 5. Literal depth-three source

For the new upper owners T_i, the source is

    E_p=T_p intersect T_(p-1) intersect T_(p-2) intersect T_(p-3).

The checker proved nonemptiness at every source position by direct mask
intersection, then checked every identity

    OR(E_i,...,E_(i+3))=T_i,
    OR(E_i,...,E_(i+2))=T_(i-1) intersect T_i.

Both the complete owner cycle and the actual 849-letter source are
included. These statements concern one cyclic component. They do not
claim that its proper upper witnesses survive an arbitrary cut or that
its lower deck is universal.

## 6. Artifacts, state assembly, and resource limits

Local artifacts:

    scratch/audit_k17_six_plus_one_parent_bank_20260908.py
    scratch/k17_six_plus_one_parent_catalogue_20260908.json
    scratch/k17_six_plus_one_selected_849_audit_20260908.json
    scratch/merged_849_upper_owner_cycle.word
    scratch/merged_849_depth3_source_cycle.word

The catalogue's current_lower_cycles and prefix_owners describe the stage
immediately before this move. To obtain the 849 stage, remove the
selected candidate's three affected_component_ids and insert the audit's
new_lower_cycle. Exclude old_115,old_116,old_118,old_122,old_129,old_138
from the cyclic collection; their owners already form the actual prefix.

Equivalently, compared with the original canonical factor, remove original
cycles 0,1,2,6,7,8 and insert the new 849-cycle and the retained 103-cycle,
as well as replacing the six bad cycles by the recorded prefix.

The remote files are in

    /home/amodo/exact-b-k17-second-c6-20260908/

with names six_plus_one_parent_catalogue.json,
six_plus_one_selected_audit.json, and the same two merged_849 word names.
The script is bank.py there and imports the previously recorded audit.py.
The bounded phases are catalogue, audit, and source. Each phase is capped
at 90 CPU seconds, 110 wall seconds, and 1 GiB address space, and each
completed in under four seconds of its remote execution call. The process
is single-threaded Python. No completed audit was restarted after the
interruption; the existing completed artifacts were read and copied.

## 7. Remaining boundary

This result verifies one more genuine fusion, reducing the GOOD cycle count
by two while retaining all current guards. It does not prove that every
candidate in the bank passes the upper or residence tests, nor that the
same bank connects every remaining component. Safe opening, the residual
rank-eight repairs, and the complete lower compiler remain unsolved.
