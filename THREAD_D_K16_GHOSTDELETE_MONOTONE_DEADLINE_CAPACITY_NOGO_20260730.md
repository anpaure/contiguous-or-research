# Thread D: the upper-complete `0x6a78` ghost-deletion rethread fails the exact deadline-mass gate (2026-07-30)

## Result

The corrected interior relocation stored in

`scratch/threadD_k16_ghostdelete_k6a78_rethread_schedule_targets_20260730.word`

does solve the two target-order requirements that motivated it:

1. its `12,873` rank-eight rows consist of every one of the
   `W=binom(16,8)=12,870` targets, plus exactly the three adjacent flat
   pairs

   ```text
   0x4e71 at 6431,6432
   0xcc63 at 12869,12870
   0xce61 at 12871,12872;
   ```

2. the unions of arbitrary nonempty consecutive target blocks contain every
   rank-nine-through-rank-sixteen mask.

Thus the earlier nonadjacent-`0x4e71` ghost has really been removed.  The
target order nevertheless cannot be the middle-delivery order of a universal
length-`12,873` word.  The obstruction is already present before COMP3:

\[
  \max \sum_i d_i=19,398
  <\sum_{r=1}^7\binom{16}{r}=26,332.
\]

The deficit is `6,934` proper prefix intervals.  This closes this one exact
`0x6a78` relocation, not the wider class of upper-complete rethreads.

## 1. Exact finite-state envelope lift

Let `T_0,...,T_(L-1)` be the prescribed target order.  Choose

\[
 d_i\in\{0,1,2,3\},\qquad q_i=i+d_i<L.
\]

For an all-delivery, ghost-free schedule, global deadline monotonicity says

\[
 \begin{cases}
 q_i=q_{i+1},&T_i=T_{i+1},\\
 q_i<q_{i+1},&T_i\ne T_{i+1}.
 \end{cases}                                      \tag{1.1}
\]

All repetitions in the present deck are contiguous, so (1.1) is exactly the
`G=0` condition, not a relaxation.  Define the maximal envelope cell

\[
 P_j=\bigcap_{i\le j\le q_i}T_i.                  \tag{1.2}
\]

The envelope lift conditions are

\[
 P_j\ne\varnothing,
 \qquad
 \bigcup_{j=i}^{q_i}P_j=T_i\quad(0\le i<L).       \tag{1.3}
\]

These are necessary for every physical compiler.  Indeed, a physical cell at
`j` belongs to every target window covering `j`, hence is a submask of `P_j`;
its row union is `T_i`, forcing the maximal-envelope union in (1.3).  They are
also sufficient for the bare system of scheduled row-union equations, by
taking the cells to be `P_j`.  This latter observation does not assert that
the maximal-envelope cells themselves have every requested lower trace.

### Proposition 1.1 (finite-state DP)

For fixed depth `D`, feasibility of (1.1)--(1.3), and the maximum of
`sum_i d_i` over all feasible lifts, are computable by a streaming finite-state
DP with at most `D+1` active rows.

**Proof.** Immediately before cell `j`, retain each unfinished row as

\[
 (i,q_i,R_i),\qquad
 R_i=\bigcup_{h=i}^{j-1}P_h.
\]

After choosing `d_j`, intersect the targets of the retained rows and `T_j` to
obtain `P_j`.  Reject a zero intersection.  Replace every `R_i` by
`R_i union P_j`; when `q_i=j`, reject unless the result is `T_i`, and otherwise
delete the expired row.  Condition (1.1) is checked against the previous
deadline.  No row starting before `j-D` remains, so the state has bounded
width.  Two histories reaching the same active state have exactly the same
legal futures.  Keeping only the larger accumulated `sum d_i` therefore gives
the exact maximum as well as feasibility.  QED.

The independent implementation is

`scratch/audit_threadD_k16_ghostdelete_monotone_deadline_dp_20260730.py`.

On the present instance its peak state count is `16`; it checks `772,120`
candidate transitions.

## 2. A local bit obstruction forces the sharp global cap

The relevant rows of the corrected target order are

```text
i=6387: K = 0x6a78
i=6388: A = 0x6639
i=6389: B = 0x6719
i=6390: C = 0x6798
i=6391: D = 0x639c.
```

### Lemma 2.1

Every feasible envelope lift has `d_6387<=1`.

**Proof.** Suppose `d_6387>=2`.  Since `K` and `A` are distinct, (1.1) gives
`d_6388>=d_6387>=2`.  Target `A` contains bit `0`, but this bit is absent from
every envelope cell in its window:

* `K` covers positions `6388` and `6389` and does not contain bit `0`;
* `C`, starting at `6390`, does not contain bit `0`;
* if `d_6388=3`, then `D`, starting at `6391`, also does not contain bit `0`.

Consequently

\[
 \bigcup_{j=6388}^{6388+d_{6388}}P_j
 \subseteq A\setminus\{0\},
\]

contradicting (1.3).  QED.

There is no repeated target before position `6431`.  Thus (1.1) makes the
offsets nondecreasing through position `6387`, and Lemma 2.1 implies

\[
 d_i\le1\qquad(0\le i\le6387).                   \tag{2.1}
\]

At the right boundary, `d_12872=0`.  The final `0xce61` flat forces
`d_12871=1`; the preceding distinct transition gives `d_12870<=1`; and the
`0xcc63` flat gives `d_12869=d_12870+1<=2`.  Monotonicity between the first and
second flat blocks therefore gives

\[
 d_i\le2\qquad(6432\le i\le12869).               \tag{2.2}

Using only `d_i<=3` on the intervening `44` positions, (2.1)--(2.2) give

\[
\begin{aligned}
 \sum_i d_i
 &\le 6388\cdot1+44\cdot3+6438\cdot2+2\\
 &=19,398.                                        \tag{2.3}
\end{aligned}
\]

The DP proves (2.3) sharp.  Its maximizing profile is

```text
d=1 on 0..6387
d=3 on 6388..6431
d=2 on 6432..12869
d=1 on 12870..12871
d=0 on 12872.
```

For this profile all maximal envelopes are nonempty and every scheduled row
union is exact.  Their rank histogram is

```text
rank 5:   43
rank 6: 6440
rank 7: 6388
rank 8:    2.
```

## 3. The compiler-independent lower-capacity contradiction

For a physical word whose first middle delivery from start `i` occurs at
`q_i=i+d_i`, there are exactly `d_i` proper prefix intervals from that start,
with endpoints `i,...,q_i-1`.  Every nonempty target of rank below eight must
be the union of at least one such proper prefix.  Since one interval has only
one union,

\[
 \sum_i d_i\ge\sum_{r=1}^7\binom{16}{r}=26,332.  \tag{3.1}
\]

Equations (2.3) and (3.1) are incompatible.  In particular, assigning cells
inside these envelopes, adding exact lower Hall rows, or invoking COMP3 cannot
repair this target order.

The obstruction explains why merely transporting the old deadline offsets
was misleading.  The transported histogram contains `6,433` depth-three
rows, but the relocated first flat and, more decisively, the `K|A|B|C|D`
collar prevent those deep rows from being placed monotonically.

## 4. Reproducible audit

```text
target order
  scratch/threadD_k16_ghostdelete_k6a78_rethread_schedule_targets_20260730.word
  SHA-256 aad8dd5ee4e0214ae0a5074d89d4ed3d0dafdec83b0a9ddcd7556e24584faba7

DP implementation
  scratch/audit_threadD_k16_ghostdelete_monotone_deadline_dp_20260730.py
  SHA-256 22c00e2885736beed55204d8232eca84d298227c2041686483421eaebcb97405

maximizing offsets
  scratch/threadD_k16_ghostdelete_k6a78_rethread_deadline_offsets_20260730.word
  SHA-256 ba118063e1c1da1d1c17840312c1e7698afdd322c6f0c4365705a7b988c1b1db

audit
  scratch/threadD_k16_ghostdelete_k6a78_rethread_deadline_dp_20260730.audit.json
  SHA-256 ad2a98bd1a722bd7501a7fff6f99799a3a6ab8a17a8c972046259269ab0825ba
  payload SHA-256 cbce2d556efd25da5c8186fb8fdcf1e1992b59ac4eac8df070a2263df047dfea
```

The exact surviving search gate is therefore narrower than before: retain
all three adjacent flats and upper completeness, but avoid placing a moved
row `K` immediately before a target whose indispensable bit is suppressed by
`K` on the left and by the next one or two starts on the right.  Equivalently,
future target-order scoring should include the maximum feasible deadline mass,
not only middle multiplicity and arbitrary-width upper deficiency.
