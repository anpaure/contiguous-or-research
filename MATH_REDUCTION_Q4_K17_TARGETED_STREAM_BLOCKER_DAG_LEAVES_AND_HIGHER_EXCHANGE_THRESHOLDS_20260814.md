# Targeted q4 streams give exact blocker-DAG leaf oracles and lossless higher-exchange banks

**Date:** 2026-08-14

**Status:** exact symbolic reduction plus five scoped emit-all structural-node
pair replays.
It identifies the information a targeted owner-column stream must retain for
blocker-DAG reachability, exact patch leaves, and fixed-depth exchange
oracles.  It does not claim that the current blocker DAG is exhausted, that
any of the five tested pair batches closes its leaf, or that a threshold
bank is complete outside its declared finite candidate universe.

## 0. Outcome

Fix an incumbent on the 680 nonfixed owner rows.  Its selected configuration
indices include the 54 reflected-pair configurations and, when a typed face
is considered, the 35 selected self lifts.  For every streamed reflected-
pair column `C`, retain

```text
 C                 its sorted ten-row mask;
 w(C)              one literal core/order witness;
 B_C               its blocker mask on selected configurations;
 a(C)              its add-only energy score;
 z_C(j)=|C intersect P_j|  for every selected configuration P_j. (0.1)
```

The row mask is not redundant: it supplies exact incoming/incoming
intersections and exact-cover incidence.  The other data have two uses.

1. At a blocker-DAG removal node `R`,

   ```text
                         B_C subseteq R
                    iff  C subseteq F(R),                    (0.2)
   ```

   where `F(R)` is the row set not covered by selected configurations
   outside `R`.
2. For every typed outgoing face `Q`,

   ```text
                   h_Q(C)=a(C)-2 sum_(j in Q) z_C(j).         (0.3)
   ```

   Thus one stream record supports every fixed-depth directed exclusion
   test at the current incumbent.

Inclusion-minimal blocker masks are complete for DAG **reachability**.
They are not a leaf exact-cover catalogue: columns with the same blocker
mask can cover different free rows.  At a leaf, exact Algorithm X can call
the anchored generator on demand with

```text
             --target-row r --allowed-rows F --catalog OUT,  (0.4)
```

and branch on every emitted row mask.  No one-swap top-K score enters this
oracle.

For a declared finite candidate universe and exchange depth `k`, a separate
two-pass stream freezes the first `k` indexed `h_Q` entries on every face
and then emits exactly the candidates passing the lossless singleton
exclusion cut.  This is complete for that universe and no larger one.

## 1. Universal blocker and directed-score record

Let the selected indexed configurations have row supports
`P_1,...,P_m`.  They need not have the same cardinality.  For a streamed
ten-row pair column `C`, define

```text
 a(C)=sum_(x in C)(2 ell_x-1),
 z_C(j)=|C intersect P_j|,
 B_C={j:z_C(j)>0}.                                            (1.1)
```

The blocker mask is the support of the overlap vector, but retaining both
is useful: `B_C` gives bitset DAG tests, while `z_C` gives the exact
multiplicities in `(0.3)`.

### Proposition 1.1 (universal directed score)

For any outgoing face `Q subseteq {1,...,m}`, the incoming linear score of
`C` in the quadratic exchange identity is `(0.3)`.

#### Proof

Adding `C` alone costs `a(C)`.  In the full square expansion, every
incoming/outgoing incidence between `C` and `P_j` contributes `-2`.
Summing those incidences over `j in Q` gives `(0.3)`.  All remaining
incoming/incoming interactions require the literal row masks and are added
later in the prefix recurrence.  \(\square\)

Consequently two columns with equal `(a,z)` may have different pairwise
intersections with future incoming columns.  They cannot be identified in
an exact higher-exchange or leaf catalogue unless their row masks also
agree.  Witnesses with the same row mask may be deduplicated at the owner
level, subject to retaining any later typed/resource decorations.

## 2. Blocker/free-row equivalence

For a removal mask `R subseteq {1,...,m}`, retain the selected family
outside `R` and put

```text
 F(R)={x:no P_j with j outside R contains x}
     =X minus union_(j outside R) P_j.                        (2.1)
```

### Theorem 2.1 (exact blocker test)

For every streamed column `C`, `(0.2)` holds.

#### Proof

If `B_C subseteq R`, every selected configuration meeting a row of `C` is
removed, so no retained `P_j` meets `C`; hence every row of `C` lies in
`F(R)`.  Conversely, if `C subseteq F(R)`, no selected configuration
outside `R` meets `C`.  Thus every index in `B_C` belongs to `R`.
\(\square\)

This equivalence is stronger than a heuristic blocker score.  It says that
the allowed-row filter at a DAG node is exactly the eligibility filter for
new pair columns.

## 3. Antichains preserve DAG reachability, not leaf options

For a row `r`, let

```text
 M_r={B_C:C is a legal pair column and r in C},
 A_r=minimal elements of M_r under inclusion.                 (3.1)
```

### Theorem 3.1 (minimal blocker children are reachability-complete)

Suppose a target removal set `T` extends the current node `R`, and a target
completion uses a column `C` through `r`.  Then some `B in A_r` satisfies

```text
                         R union B subseteq T.                 (3.2)
```

If no column through `r` is already eligible at `R`, this child is a strict
extension of `R`.

#### Proof

Eligibility of the target column gives `B_C subseteq T`.  The finite menu
`M_r` contains a minimal element `B subseteq B_C`, obtained by descending
from `B_C` while possible.  Then `(3.2)` follows.  If `B subseteq R`, the
column realizing `B` would already be eligible, contrary to the stated
branch condition.  \(\square\)

The same argument applies to the blocker menu of a destroyed self group,
with the selected member of that group included in every blocker.

The theorem does **not** permit discarding all nonminimal columns.  A
blocker mask records conflicts with the incumbent, not which other free
rows the column covers.  Two columns having the same `B_C`, or one having a
larger blocker, can be inequivalent or indispensable in a disjoint exact
cover of `F(R)`.  Therefore:

```text
 blocker antichain = exact DAG branch certificate;
 full row-mask menu = exact leaf patch data.                  (3.3)
```

## 4. On-demand exact Algorithm-X leaf oracle

Assume the incumbent row loads lie in `{0,1,2}`.  Its defect multigraph has
one vertex per selected configuration and, for every load-two row, one edge
joining the two selected configurations containing that row.  Assume `R`
is a vertex cover of this graph.  Then the retained selected configurations
outside `R` are row-simple.  Their uncovered rows are exactly `F=F(R)`.
Let `G` be the set of destroyed self groups and let `p` be the number of
destroyed reflected-pair configurations.

The selected profile has total nonfixed-row incidence
`35*4+54*10=680`.  Removing `|G|` self lifts and `p` pairs deletes
`4|G|+10p` incidences.  The outside family therefore has
`680-(4|G|+10p)` remaining incidences.  Because it is simple, those
incidences occupy that many distinct rows.  Taking the complement in the
680-row ground gives the exact conservation law

```text
                          |F|=4|G|+10p,                       (4.1)
```

because a reduced self lift uses four nonfixed rows and a reflected-pair
configuration uses ten.

A patch is legal exactly when it chooses one option from the **full legal
self menu** `H_g` of every group `g in G`, chooses `p` pair columns, every
chosen support lies in `F`, and those supports partition `F`.  The removed
incumbent self option belongs to `H_g` and may be reselected when its rows
lie in `F`; this is necessary at redundant or nonminimal removal masks.

### Algorithm 4.1

Maintain a state `(F,G,p)`.

1. If `G` is nonempty, choose a group `g in G`.  Branch over every option
   `V in H_g` with `rows(V) subseteq F`, replacing
   the state by

   ```text
                 (F minus rows(V), G minus {g}, p).           (4.2)
   ```

2. Once `G` is empty and `p>0`, choose any row `r in F`.  Run the complete
   anchored target stream at `r`, retain every distinct pair mask
   `C subseteq F`, and branch to

   ```text
                         (F minus C, empty, p-1).              (4.3)
   ```

3. Accept exactly at `(empty,empty,0)`.  Reject a state with an empty
   required menu, `|F|!=4|G|+10p`, or a nonempty `F` when no branch exists.

### Theorem 4.2 (leaf completeness)

Algorithm 4.1 finds a patch if and only if the full legal self/pair
catalogue contains one.

#### Proof

In any legal patch, the target patch contains one chosen option from group
`g`, its rows lie in `F`, and step 1 includes that branch.  After all group
choices, any legal pair patch covers the chosen row `r` with one unique pair mask
`C subseteq F`.  Completeness of the anchored generator ensures that step
2 emits it.  Deleting the chosen support preserves the same statement on
the residual patch, so induction reaches the accepting state.  Conversely,
every branch uses an allowed typed configuration and deletes its rows;
therefore an accepting branch gives disjoint supports of the forced type
profile whose union is the original `F`.  \(\square\)

Group-first branching is only a convenient canonical order.  An
interleaved exact-cover implementation may choose the smallest current row
or menu, provided its row branch includes **every** eligible option through
that row from every remaining self group, including a reselectable
incumbent, and every emitted pair mask.

## 5. Existing emit-all CLI is the exact pair branch

The current targeted C++ generator already implements step 2.  With no
swap-scoring context,

```text
 search_q4_k17_owner_targeted_reflection_pairs
   --target-row r
   --instance INSTANCE
   --allowed-rows F_FILE
   --catalog OUT
   --threads T.                                               (5.1)
```

reads an arbitrary whitespace-separated allowed set, rejects it if it
omits `r`, filters every generated mask by `C subseteq F`, deduplicates by
the complete sorted ten-row mask, and writes every retained mask with one
literal core/order/owner witness.  Thus `--allowed-rows` is the requested
allowed-row-file interface and unscored `--catalog` mode is the requested
emit-all interface; no new alias is mathematically necessary.

This is not a claim that an arbitrary leaf is small.  The catalogue can be
large, and writing every mask is essential to the completeness assertion.
The literal implementation used below is
`scratch/search_q4_k17_owner_targeted_reflection_pairs_20260814.cpp`;
its H100-compiled binary was
`/dev/shm/search_q4_k17_owner_targeted_reflection_pairs`.  Section 7 binds
both bytes together with the generic independent catalogue replay.

## 6. Lossless higher-exchange threshold stream

Fix a declared finite pair-candidate universe `U`, an outgoing face `Q` of
size `k`, and its exact constant `c_Q`.  For a distinct incoming prefix
`S subset U`, let

```text
 q_Q(S)=sum_(C in S)h_Q(C)
       +2 sum_({C,D} subset S)|C intersect D|,

 mu_t^Q(S)=minimum sum_(C in T)h_Q(C)                         (6.1)
```

over `t` distinct candidates `T subseteq U-S`.  A prefix lying in a
negative `k`-exchange necessarily satisfies

```text
                    c_Q+q_Q(S)+mu_(k-|S|)^Q(S)<0.             (6.2)
```

All omitted overlaps are nonnegative.  After sorting `U` by `(h_Q,index)`,
the first `k` indexed entries compute every exclusion minimum in `(6.2)`.

### Exact two-pass interface

1. Stream all of `U` and freeze the first `k` indexed `h_Q` entries for
   every outgoing face under consideration.
2. Stream the same deduplicated indices again.  For **every** face `Q` on
   which the singleton cut

   ```text
                 c_Q+h_Q(C)+mu_(k-1)^Q({C})<0                (6.3)
   ```

   holds, emit a separate record `(C,Q,h_Q(C))`.  Discard `C` only when no
   declared face satisfies `(6.3)`.
3. Run the canonical prefix recurrence on the emitted face banks, using
   their row masks for every exact incoming/incoming overlap.

Every member of a negative exchange passes `(6.3)`, so the interface is
lossless.  For a typed mixed face, replace the same-type exclusion minimum
by the literal minima of its labelled self-group menus; the universal
overlap vector in `(0.1)` still computes `h_Q(C)`.

The universe declaration is load-bearing.  If pass 1 includes only the
current finite pool and one target-row stream, its thresholds are complete
only for their union.  An unseen column can lower an exclusion minimum and
invalidate a discard.  Consequently neither a one-swap top-K bank nor a
single-row threshold bank proves an all-atlas higher-exchange no-go.

## 7. First five structural-node pair replays

On one sampled blocker-DAG root of size 18, the exact free set has size
162.  The emit-all interface gave:

```text
target row14: allowed raw rails 50, distinct masks 25, all 25 new;
target row42: allowed raw rails 46, distinct masks 23, all 23 new.       (7.1)
```

Independent literal replay checked every mask and witness, target
incidence, containment in the 162-row free set, quotient simplicity,
reflection disjointness, and absence from the respective current pool.
These are exact column-generation batches, not leaf solutions.  That root
still had zero-menu self groups, so Algorithm 4.1 next required
group-blocker children.  On the resulting child every destroyed self group
had at least one eligible option (there was no zero-menu group), but its
destroyed-group set `G` was not empty.  Its free set had size 186 and the
next exact pair stream gave

```text
target row228: allowed raw rails 150, distinct masks 75, all 75 new.     (7.2)
```

All 75 row228 masks received the same independent literal replay.  This
batch is one component of an interleaved row branch: completeness also
requires every eligible option through row228 from every remaining self
group, including a reselectable incumbent.  The pair masks therefore do
not by themselves prove that the remaining exact cover is feasible.

On a sibling child with no zero-menu self group and a 196-row free set, the
same pair oracle gave

```text
target row625: allowed raw rails 72, distinct masks 36, all 36 new.      (7.3)
```

All 36 masks again passed literal witness and allowed-row replay.  This is
a separate sibling-node batch, not an addition to the row228 free set.
Moreover, `(4.1)` and `|F|=196` force `G` to be nonempty, so this is only
the pair component of an interleaved row branch; eligible self options
through row625 must also be included.

On another sibling with no zero-menu self group and a 186-row free set, the
pair oracle gave

```text
target row89: allowed raw rails 240, distinct masks 120, all 120 new.    (7.4)
```

All 120 masks passed the same replay.  As with row228, `(4.1)` and
`|F|=186` force destroyed self groups to remain, so this is only the pair
component of an interleaved row branch.
It is a sibling-specific catalogue; the several free sets in
`(7.1)--(7.4)` must not be unioned into one patch instance without the
corresponding blocker-DAG lineage.  None of these five batches alone closes
a leaf.

### 7.1 Bound H100 evidence

The five catalogues were generated by the source and binary named in
Section 5.  Each was then replayed by
`scratch/audit_q4_k17_owner_targeted_allowed_emitall_20260814.py`, which
reconstructs the anchored owner rail from the stored core/order witness,
recomputes its reflected mate and reduced ten-row mask, checks target and
allowed-set membership, checks quotient simplicity and reflection
disjointness, and compares against the input pool.  The exact paths and
SHA-256 values are recorded in the accompanying audit.  In particular,
the five H100 report/catalogue/replay triples bind, respectively, the
`(row14,F162)`, `(row42,F162)`, `(row228,F186)`, `(row625,F196)`, and
`(row89,F186)` counts in `(7.1)--(7.4)`.

## 8. Scope

Proved here:

* the universal stream signature `(C,B_C,a,z)`;
* exact blocker/free-row equivalence;
* reachability completeness of minimal blocker antichains;
* the sharp distinction between branch antichains and leaf row masks;
* on-demand Algorithm-X completeness using emit-all target streams; and
* the exact two-pass threshold interface for a declared finite universe.

Not proved here:

* exhaustion or feasibility of the live blocker DAG;
* smallness of any allowed-row catalogue or threshold bank;
* completeness beyond the candidate universe included in pass 1;
* simultaneous lower/upper ticket feasibility of emitted owner columns; or
* physical actuator/resource/residence compilation.
