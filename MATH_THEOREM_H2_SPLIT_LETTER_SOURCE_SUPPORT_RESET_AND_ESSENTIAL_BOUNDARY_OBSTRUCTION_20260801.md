# Split-letter source support, exact side-cell Hall, and the essential-boundary reset gate

Date: 2026-08-01  
Lane: H2, regenerative sidecar / bounded task birth  
Status: exact abstract interval-word theorem and exact obstruction.  The
positive result is conditional on an admissible Pascal host and on a certified
simultaneous contraction.  It is not an all-dimensional host theorem.

## 0. Outcome

Replacing a source letter `X` by a consecutive nonempty block with union `X`
preserves every old interval OR.  For several simultaneous refinements, the
genuinely new physical cells are exactly the intervals which cut one refined
block at their left endpoint, their right endpoint, or both.  In the binary
case `X=Z union T`, an occurrence-labelled task family is carried by at most
`H` actual old source letters **if and only if** its equality graph to those
partial-block cells has a saturating matching.  The transported old cells and
the new side cells are disjoint, so the two matchings combine without any
old-target loss.

The intrinsic one-transition length parameter is not the number of host
letters.  For a core word `W` and task bank `U`, define

\[
 \beta_W(U)=\min_{\mathcal B}
       \sum_p(|B_p|-1),                                    \tag{0.1}
\]

where `B_p` ranges over consecutive nonempty replacement blocks with union
`A_p`, and the refined word realizes `U`.  Old values need not be included
in `U`: they survive automatically.  Thus `beta_W(U)` is exactly the least
additive length of a lossless split-letter **coverage** repair.  For an
occurrence-labelled bank and old matching `M`, write
`beta_(W,M)^adm(U)` for the same minimum with an injective assignment to
arbitrary admissible refined cells disjoint from the full-block lifts of
`C(M)`, with every one of those `M`-lifts itself required to be admissible.
This guarded parameter is the exact matching-safe cost.  For genuinely new
target values its task cells are automatically side cells.  Binary
source-support is the proof-friendly cost-one-column subclass.

This gives a genuine bounded-birth theorem for one transition, but not by
itself a regenerative `B+O(1)` theorem.  A split boundary can remain essential
to a target created at an earlier transition.  Let `Phi` be the minimum number
of marked split boundaries which must remain after a simultaneous
matching-safe contraction.  If one transition reclaims at least a fraction
`theta` of the old essential boundaries and births tasks on at most `H` fresh
binary splits, then

\[
                 \Phi'\le (1-\theta)\Phi+H.                 \tag{0.2}
\]

Thus `theta>0` gives the invariant bound `Phi<=H/theta` (up to integer
rounding), and full reset gives `Phi'<=H`.  Without a reclaim hypothesis the
only valid recurrence is `Phi'<=Phi+H`.

Both qualifications are sharp.  First, one actual source letter can have
arbitrarily large refinement cost: for the one-letter word `W=([n])`, all
singleton tasks lie below that host but `beta_W({{1},...,{n}})=n-1`.
Second, for every `t` there is a word with `t` independent
letters `X_i=K+{a_i,b_i}`.  At step `i`, split `X_i` into
`K+{a_i},K+{b_i}` and prescribe the singleton target `K+{a_i}`.  Every old OR
survives and each step uses one actual source letter, but after `t` steps all
`t` boundaries are essential.  Contracting the `i`-th pair destroys its
target.  Therefore bounded source support per transition does not imply
bounded accumulated slack; the omitted debt term is the number of
nonreclaimable split boundaries (or an equivalent normalized-length state).
The first obstruction is spatial compression; the second is temporal reset.

## 1. Simultaneous split algebra

Let

\[
                         W=(A_1,\ldots,A_N)                 \tag{1.1}
\]

be a word of nonempty sets.  Choose `P subset [N]`.  For every `p in P`
choose nonempty `Z_p,T_p` with

\[
                         A_p=Z_p\cup T_p.                  \tag{1.2}
\]

Let `E_sigma(W)` be obtained by replacing each selected letter by the ordered
block `Z_p,T_p`.  The **full-block lift** of an old interval is the expanded
interval containing every piece of every old block it meets.

### Theorem 1.1 (simultaneous block-contraction preservation)

The full-block lift is an injection on old physical intervals and preserves
their literal OR values.  Consequently every old interval-OR target survives
all the splits simultaneously.

#### Proof

The selected old blocks are disjoint.  The lift of an interval is still an
interval, and each split block contributes `Z_p union T_p=A_p`.  The first
and last old block indices recover the old interval, proving injectivity.
\(\square\)

Call an expanded interval a **side cell** if it is not a full-block lift.

### Theorem 1.2 (exact side-cell normal form)

Every side cell has one of the following forms.

1. It is the singleton `Z_p` or `T_p` inside one split block.
2. Its leftmost old block is `p`, its rightmost old block is `q>p`, every
   interior block is complete, and its value is

\[
 L_p\ \cup\!\bigcup_{p<i<q} A_i\ \cup R_q,                \tag{1.3}
\]

where `L_p` is either `A_p` or, when `p` is split, `T_p`, and `R_q` is either
`A_q` or, when `q` is split, `Z_q`; at least one endpoint choice is partial.

Conversely every interval described above is a side cell.

#### Proof

An interval meets a consecutive set of old blocks.  Every strictly interior
block is met completely.  At the left endpoint, the only way to omit part of
a binary split block and continue right is to start at its second piece
`T_p`.  Dually, at the right endpoint the only partial choice is to end at
`Z_q`.  If both endpoints lie in one split block, the only non-full intervals
are its two singleton pieces.  These observations also prove the converse.
\(\square\)

This normal form includes the two nested rays from one split and the grids
between two different splits.

### Theorem 1.3 (arbitrary-block boundary-fragment normal form)

More generally replace `A_p` by a nonempty block

\[
 B_p=(B_{p,1},\ldots,B_{p,\ell_p}),\qquad
                  \bigcup_j B_{p,j}=A_p.                 \tag{1.4}
\]

Every old interval has the injective full-block lift of Theorem 1.1.  Every
expanded interval which projects to one old position `p` is a consecutive
subblock of `B_p`.  Every expanded interval projecting to `[p,q]`, `p<q`,
has value

\[
 \left(\bigcup_{j=s}^{\ell_p}B_{p,j}\right)
 \cup\!\bigcup_{p<i<q}A_i
 \cup\left(\bigcup_{j=1}^{t}B_{q,j}\right)             \tag{1.5}
\]

for some suffix index `s` and prefix index `t`; unsplit endpoint letters are
read as one-piece blocks.  Conversely every such consecutive subblock or
suffix--interior--prefix expression is a physical interval.  Hence (0.1) is
an exact optimization over actual source occurrences, not merely a
containment relaxation.

#### Proof

An expanded interval meets a consecutive set of old blocks.  It meets every
strictly interior block completely, and meets each endpoint block in a
consecutive suffix or prefix; when both endpoints project to the same block,
their intersection is one consecutive subblock.  The union identities in
(1.4) give the full-block lift, and the converse follows by choosing the
displayed endpoints. \(\square\)

## 2. Exact task grouping under actual source letters

Let `U` be a set of genuinely new target vertices, or an occurrence-labelled
task multiset when separate physical cells are required.  Form the bipartite
graph `G_sigma(U)` whose right vertices are admissible side cells and where

\[
                         uJ\in E(G_\sigma)
       \quad\Longleftrightarrow\quad \operatorname{OR}(J)=u.       \tag{2.1}
\]

Here *admissible* may impose a deadline/width bound.  If a final compiler cap
is present, it must also certify the displayed expanded source word; OR
preservation alone does not imply cap legality.

### Theorem 2.1 (source-support Hall characterization)

The tasks `U` can be assigned injectively to new physical cells created by
splitting the source positions `P` if and only if

\[
                   |N_{G_\sigma}(Y)|\ge |Y|
                         \qquad(Y\subseteq U).              \tag{2.2}
\]

If `M` is an old target-to-cell matching and every full-block lift of a cell
of `M` is admissible after the transition, then any matching supplied by
(2.2) is cell-disjoint from the transported `M`.  If the new target vertices
are disjoint from those saturated by `M` (duplicates are instead discarded
as redundant target rows), their union is a matching saturating both banks.

#### Proof

Hall's theorem gives the first equivalence.  By definition no side cell is a
full-block lift, while every transported old matching cell is a full-block
lift.  Thus the cell sets are disjoint.  Target disjointness gives the other
shore.  Theorem 1.1 preserves every transported equality.  \(\square\)

Define the **binary source-support number** of `U` in `W` to be the minimum
`|P|` over split data satisfying (1.2), admissibility, and (2.2), and put it
equal to infinity if no such data exist.  This is the weakest exact meaning
of “the task bank is grouped under `H` actual source letters” for binary
columns.  It equals the additive length in that subclass.  For arbitrary
blocks, the exact additive parameter is `beta_W(U)` from (0.1); the number of
positions whose letters contain all tasks is only a host-cover relaxation.
A count of task types, a common envelope, or marginal ray cardinality is
insufficient.

For one fixed split, Theorem 1.2 reduces (2.2) to the exact two-ray equality
test.  In particular a right ray has values

\[
 T_p,\quad T_p\cup A_{p+1},\quad\ldots,
 \quad T_p\cup A_{p+1}\cup\cdots\cup A_j,                 \tag{2.3}
\]

and the left ray is the reversal.  In the rotating-hole finish, the only
genuinely new side-cell task is the singleton `tau`.  The displaced old cell
and all `h-1` casualties are instead full-block lifts of old reference
intervals, so Theorem 1.1 preserves them automatically.  This sharper fact,
not a claim that the casualties are new side cells, is why one split carries
the complete family.

### Corollary 2.2 (singleton-host sufficient condition)

Restrict to serving each genuinely new task as one literal member of a
replacement block.  Such service is possible exactly when every nonempty
task `T` is contained in some actual old letter `A_p`.  Necessity follows
from `T subseteq union B_p=A_p`.  For sufficiency, assign tasks
`T_1,...,T_s` to a containing letter `X` and use the block

\[
                         X,T_1,\ldots,T_s.             \tag{2.4}
\]

Its union is `X`, every task is a singleton, and all old intervals survive.
This construction costs one position per assigned task, not one per host.
Consequently bounded host-cover number alone does not imply bounded
`beta_W`; Proposition 4.2 gives a sharp one-host obstruction.

### Corollary 2.3 (one-transition bounded-birth theorem)

Suppose a same-parity Pascal transition first supplies a child source word
`W^0` which:

1. realizes every inherited target and carries an old matching `M` into
   admissible child cells;
2. has a new task bank `U` with
   \(\beta^{\rm adm}_{W^0,M}(U)\le H\) (in particular, matching-safe binary
   source-support number at most `H` is sufficient);
3. admits a witnessing expansion whose literal word satisfies all child
   owner, q1, residence, upper, topology, deadline and common-cap rows, and
   in which every full-block lift of an `M`-cell is admissible.

Then at most `H` added source letters produce a child word realizing every
inherited target and every task, with zero old matching loss.  The number of
tasks may be unbounded; only their exact block-refinement cost is bounded.

This is nontrivial but one-step.  An additive induction additionally needs a
uniform slack/reset clause for `W^0`.

### Corollary 2.4 (the rotating-hole ray is a true cost-one reset)

In the authenticated `H=1` rotating-hole source, the old letter is

\[
                         X=\tau\cup\{\epsilon\}.
\]

The refinement `({epsilon},tau)` has cost one.  Its only genuinely new
required value is the singleton `tau`.  Every one of the `h-1` alleged
complete-damage casualties, the displaced old cell, every old upper witness,
and the old screen row are full-block lifts and therefore survive with no
matching loss.  The carrier values remain literal; precisely the crossing
carrier cells use deadline `h+2` instead of `h+1`.  Hence the family has
`beta=1` and zero target sidecar after paying one physical position.

The zero-**matching**-loss conclusion holds in unrestricted interval cells,
or in a compiler which explicitly accepts the one-unit deadline staircase.
The longest casualty lift grows from width `h` to `h+1`; a rigid width-`h`
compiler may still reject it.

This is not yet a recursive reset: the next transition must either accept
the one-unit deadline staircase or factor through contraction while carrying
the singleton `tau` into its new task ledger.

## 3. Exact contraction and reset

Now start from a word `V` with a marked ordered refinement presentation

\[
 A_p\longmapsto(B_{p,1},\ldots,B_{p,\ell_p}),qquad
                         \bigcup_jB_{p,j}=A_p.             \tag{3.0}
\]

A **coarsening** deletes any chosen internal boundaries and replaces every
maximal consecutive run of pieces by its union.  These runs are disjoint, so
all chosen merges are simultaneous.  Full contraction deletes every internal
boundary and returns the core word.  For an interval `J` of `V`, let
`cl_R(J)` be the smallest interval in the coarsened word containing the
images of its positions.  Closure adds every omitted piece of the left and
right endpoint coarse blocks; every strictly interior coarse block is already
complete.

### Theorem 3.1 (exact protected-target contraction criterion)

A protected target `S` survives the simultaneous contraction of `R` if and
only if it has a witness interval `J` in `V` such that

\[
       \operatorname{OR}(J)=S,
       \qquad \operatorname{OR}(cl_R(J))=S.               \tag{3.1}
\]

Equivalently, the union of all omitted endpoint pieces inserted by closure is
already a subset of `S`.

For an occurrence-labelled protected bank or a target-cell matching, safe
simultaneous contraction is equivalent to Hall's condition in the graph from
targets to contracted physical cells whose full-block expansions have value
equal to the target.  This matching condition is necessary because distinct
old cells can coalesce under contraction.

#### Proof

Every coarsened interval expands to a full-coarse-block interval of `V` with
the same value.  Conversely, closing a `V` interval under `R` adds only the
omitted pieces of its two possible partial endpoint blocks.  It represents
the same target after coarsening exactly when those added bits were already
in its OR, proving (3.1).  The cell-assignment statement is Hall's theorem.
\(\square\)

For a marked refinement state `(V,P,M)`, define

\[
 \Phi(V,P,M)=\min\{\text{number of refinement boundaries retained}:
        \text{the coarsening preserves }P\text{ and }M\}.        \tag{3.2}
\]

The minimum is taken only over literal coarsenings certified by Theorem 3.1
and the matching Hall condition.  This history-aware term is the physical
slack that a target-only sidecar omits.

### Theorem 3.2 (split-reset and contraction recurrence)

Assume the next Pascal/core transition explicitly factors through a certified
contraction which reclaims `g` of the `Phi` indispensable boundaries in a
chosen minimum state.  Assume its exhaustive new task bank has a literal
block refinement of cost `r<=H`, and that every transported deadline and
final physical/common-cap guard accepts the contracted-then-refined word.
Then

\[
                         \Phi'\le\Phi-g+r.                 \tag{3.3}
\]

Consequently:

* full reset (`g=Phi`) gives `Phi'<=H`;
* if `g>=theta Phi` for one fixed `theta>0`, then (0.2) holds and
  `Phi<=ceil(H/theta)` is an invariant region after enlarging the finite base;
* with no reclaim theorem, only `Phi'<=Phi+H` follows.

If word length rather than marked-boundary count is the induction state, the
same conclusion requires that the presplit child use at most
`B(k+2)+c-r` positions.  Otherwise even a perfect task reset can exceed the
additive budget.

#### Proof

Perform the certified old contractions and then the cost-`r` refinement.  The
old protected system survives by Theorem 3.1; Theorem 1.3 and the literal
task-to-cell Hall certificate add the new tasks.  The resulting marked
presentation leaves at most `Phi-g+r` boundaries.  The displayed
consequences are immediate. \(\square\)

## 4. Sharp accumulation obstruction

Fix a nonempty core `K`, and choose pairwise distinct labels
`a_i,b_i` outside it.  Put

\[
 X_i=K\cup\{a_i,b_i\},\quad
 Z_i=K\cup\{a_i\},\quad T_i=K\cup\{b_i\}
                         \qquad(1\le i\le t).             \tag{4.1}
\]

Start from `W_0=(X_1,...,X_t)`.  At transition `i`, replace `X_i` by
`Z_i,T_i` and add the new target `S_i=Z_i`.

### Proposition 4.1 (one supported task per step, unbounded essential debt)

Every transition preserves every previously occurring interval OR and has
binary source-support number one.  After `t` transitions all `S_i` occur,
but every one of the `t` split boundaries is essential: contracting the
`i`-th pair removes `S_i` from the entire interval-OR language.  Hence

\[
                              \Phi=t.                      \tag{4.2}
\]

#### Proof

Preservation follows from Theorem 1.1.  The singleton cell `Z_i` witnesses
`S_i`.  Every other letter contains a private label different from `a_i`,
and every interval containing more than the singleton `Z_i` therefore has a
bit outside `S_i`.  After contracting its pair, `Z_i` is absent and the
letter `X_i` contains the extra private bit `b_i`; so no interval equals
`S_i`.  This holds independently for every `i`. \(\square\)

The construction is an abstract interval-word obstruction, not a no-go for a
special Pascal/Johnson host.  It proves that any regenerative theorem must
carry either the essential-boundary term `Phi`, a simultaneous contraction
certificate, or an equivalent normalized-length/slack invariant.

### Proposition 4.2 (one actual host can require unbounded refinement cost)

Let the core word have the single actual source letter

\[
                         W_n=([n]),                         \tag{4.3}
\]

and require the `n` singleton tasks

\[
                         {\cal U}_n=\{\{1\},\ldots,\{n\}\}. \tag{4.4}
\]

Every task is contained in the same source letter, so the ordinary host-cover
number is one.  Nevertheless

\[
                         \beta_{W_n}({\cal U}_n)=n-1.       \tag{4.5}
\]

#### Proof

In any nonempty-set word, an interval with OR exactly `{i}` contains only
letters contained in `{i}`, hence contains a literal letter `{i}`.  Distinct
singleton targets therefore require at least `n` physical letters.  Refining
the one old letter into the block `{1},{2},...,{n}` attains this bound, so the
additive cost is exactly `n-1`. \(\square\)

The smallest strict binary warning is `n=3`: both tasks `{1},{2}` lie below
the one host `{1,2,3}`, but one two-part split cannot realize both.  It would
force its two pieces to be `{1}` and `{2}`, whose union omits `3`.  Two added
positions are sufficient.  This obstruction concerns abstract interval
words; it does not prove that a genuine Pascal task bank has unbounded
`beta`.

## 5. Exact surviving gate

The split lemma removes complete-damage accounting once the following
correlated host is actually supplied:

1. actual source letters with a literal block refinement of total cost at
   most `H`, whose partial-block side-cell graph Hall-saturates the entire
   new task bank;
2. admissible transported deadlines for the old compiler matching;
3. one literal expanded word satisfying owner/q1/residence/upper/topology and
   final common-cap rows; and
4. a next-transition factorization through a reset certificate reclaiming
   all, or a fixed positive fraction, of the previously essential split
   boundaries before the next task birth.

Items 1--3 give zero accumulated **target loss**.  Item 4, or an equivalent
presplit length reserve, is what gives bounded accumulated **physical
sidecar**.  The split-letter pivot does not supply item 4 automatically.
The precise remaining Pascal statement is a uniform bound on admissible
`beta`, together with contraction alignment; `O(1)` raw host count is
neither condition.

## 6. Audit and scope

Run

```text
python3 scratch/audit_h2_split_letter_block_contraction_independent_20260801.py
python3 scratch/audit_h2_split_letter_source_support_reset_20260801.py
```

The first audit independently exhausts 75,166 valid binary splits of all
nonzero three-bit words of length at most four, checks simultaneous splitting
at every position, the exact endpoint-ray/trace normal form, and reconstructs
the rotating-hole repair for `2<=h<=64`.  The second replays the side-cell and
contraction criteria on 343 words and 924 split systems, the essential-
boundary accumulation family through ten steps, and the one-host refinement
obstruction through ground size twelve.

The source pivot itself is authenticated by
`MATH_THEOREM_H1_SPLIT_LETTER_RAY_ABSORPTION_AND_ONE_COLUMN_CRITERION_20260801.md`.
The independent scope audit is
`MATH_AUDIT_H2_SPLIT_LETTER_BLOCK_CONTRACTION_AND_TASK_HOSTING_20260801.md`.

No computation or theorem here supplies an all-dimensional Pascal child,
inserted-source Johnson adjacency, fixed-width common-cap acceptance, or a
rooted/q1/residence host.  Proposition 4.2 and the accumulation family are
abstract interval-word obstructions, not no-go theorems for the structured
Pascal catalogue.
