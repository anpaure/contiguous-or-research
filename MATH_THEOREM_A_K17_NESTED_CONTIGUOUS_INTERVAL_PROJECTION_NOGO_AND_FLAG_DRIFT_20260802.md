# K17 nested contiguous-address no-go and long-flag drift

**Date:** 2026-08-02  
**Lane:** A, integral rotor fusion  
**Status:** exact finite K17 obstruction on the frozen depth-three
owner/payload table.  The obstruction is already visible in the union
projection, before one asks for a common state choice or a directed cycle.

## 0. Result and exact scope

Let

```text
scratch/k17_exact_depth3_owner_payload_table_20260802/
  k17_depth3_owner_payload.tsv
```

be the frozen `24,310`-row K17 chain table.  Its rows have lengths

\[
                 (n_1,n_2,n_3)=(1748,3899,18663).       \tag{0.1}
\]

The **hard heads** are the `18,646` length-three rows whose bottom target
has rank greater than one.

This note allows every row to place its named chain targets on a strictly
nested chain of nonempty contiguous intervals in a three-cell source state.
There are exactly

\[
                       6,\quad 9,\quad 4                \tag{0.2}
\]

address flags for rows of lengths one, two and three.  A source row is
joined to a hard head whenever at least one source flag and one of the four
long-head flags have a common literal three-cell state satisfying the owner
transition.

The resulting bipartite projection has

\[
\begin{array}{c|ccc}
\text{supplier length}&1&2&3\\ \hline
\text{allowed row--head pairs}&5764&16849&49193
\end{array}                                             \tag{0.3}
\]

and `418` hard heads have degree zero.  Its exact Hopcroft--Karp maximum is

\[
                         18162/18646,                    \tag{0.4}
\]

so its deficiency is `484`.  The saved maximum uses

\[
                         937,quad3375,quad13850          \tag{0.5}
\]

suppliers of lengths one, two and three.

Consequently the frozen table has no one-copy predecessor assignment in
this one-transition, strictly nested contiguous-address class.  Any
injective one-transition assignment on the **same 24,310 supplier-row
shore** in a supergraph of this catalogue must use at least `484` outside
arcs, at least `418` of them entering the named zero-heads.

The word **nested** is essential.  The result does not enumerate, for
example, a smaller target placed on cell `A` and a larger target placed on
`BC`; those intervals are not nested.  Nor does it cover a multi-transition
or multi-row macro, a changed chain table, or reassigned owner/payload rows.

## 1. Complete nested address family

Encode the six nonempty contiguous intervals of three positions by

\[
                         1,2,4,3,6,7.                    \tag{1.1}
\]

For a row

\[
                         C_1\subset\cdots\subset C_\ell=U,
                    \qquad 1\leq \ell\leq3,             \tag{1.2}
\]

an address flag is a strict inclusion chain

\[
                         I_1\subset\cdots\subset I_\ell \tag{1.3}
\]

of intervals from (1.1), with the cells in `I_q` required to have union
`C_q`.  Direct enumeration gives

\[
\begin{aligned}
\ell=1:
  &\quad 1,2,4,3,6,7;\\
\ell=2:
  &\quad (1,3),(1,7),(2,3),(2,6),(2,7),\\
  &\qquad (4,6),(4,7),(3,7),(6,7);\\
\ell=3:
  &\quad (1,3,7),(2,3,7),(2,6,7),(4,6,7).
                                                               \tag{1.4}
\end{aligned}
\]

Thus (0.2) is exhaustive for the declared class.

### Lemma 1.1 (exact cell-interval test)

Fix one source flag and one hard-head flag.  Intersect, separately at each
of the three source cells, all Boolean lower and upper bounds imposed by:

1. the source row's interval unions;
2. the two retained cells of the head flag; and
3. the discarded outer predecessor cell, which must contain the owner
   increment `T-U`.

Write the resulting cell interval as `[lo_p,hi_p]`.  The two flags share a
literal transition if and only if

\[
       hi_p\ne\varnothing,qquad lo_p\subseteq hi_p
                         \quad(p=1,2,3),                 \tag{1.5}
\]

and, on setting each cell equal to its maximal feasible value `hi_p`, every
source interval has exactly its prescribed union.

#### Proof

Necessity is immediate.  For sufficiency choose the maximal feasible cells
`hi_p`.  Every cell belonging to a prescribed source interval was already
upper-bounded by that interval's target.  Hence its union cannot overshoot;
the final equality test says it does not undershoot.  Conditions (1.5)
make all source letters nonempty and include every required head increment.
The outer-predecessor bounds give the frozen owner.  Finally, the long-head
four-flag normal form supplies the omitted new third cell: choose a member
of its nonempty component interval containing that cell's compulsory chain
increment.  Hence the maximal retained-cell choice extends to a complete
literal transition.  \(\square\)

This is why an intersection supported only by the empty set must be
rejected.  The frozen source explicitly checks `hi_p != 0`.

## 2. Projection obstruction

Let `S` be the `24,310` occurrence-labelled table rows and let `H` be the
`18,646` hard heads.  Put an edge `j i` in `G_nest` precisely when the exact
test of Lemma 1.1 accepts at least one of the `6/9/4` source flags of `j`
and one of the four head flags of `i`.  The union over flags is deliberate:
it forgets whether the same state choice can serve both the incoming and
outgoing transition of a row.

### Theorem 2.1 (exact K17 nested-address projection no-go)

The graph `G_nest` has the statistics (0.3)--(0.5), including `418`
isolated right vertices and maximum matching `18,162`.  In particular no
selection of one distinct predecessor row for every hard head exists.

#### Proof

The catalogue source exhausts (1.4), applies Lemma 1.1 to every ordered
row--hard-head pair, and then runs Hopcroft--Karp.  The frozen run reports
`71,806` allowed pairs split as in (0.3), `418` degree-zero heads, and the
maximum (0.4).  The emitted matching has `18,162` distinct suppliers and
`18,162` distinct heads; an independent implementation reconstructs the
complete flag-pair bit mask of every selected edge and reproduces (0.5).

Any balanced one-copy chronology would induce an injection from hard heads
to predecessor rows in this projection.  The isolated heads already refute
such an injection without using matching optimality.  Hopcroft--Karp sharpens
the obstruction to deficiency `484`.  Finally, if an injective assignment
on the same supplier-row shore in a supergraph of `G_nest` used fewer than
`484` outside arcs, deleting those arcs would leave a matching in `G_nest`
larger than `18,162`, a contradiction.  This deletion argument is not a
claim about a multi-transition or multi-row macro which need not induce such
a matching.  \(\square\)

The maximum is certified by the audited deterministic Hopcroft--Karp run.
The saved edge witness independently certifies the matching lower bound and
all selected literal masks; a separate serialized Koenig cover was not
emitted.  This distinction does not affect the scoped no-go, which already
follows from the `418` isolated hard heads.

## 3. Long-flag monotonicity

For a long row `L subset M subset U`, order its four flags as

\[
        0=12/1<1=12/2<2=23/2<3=23/3.                  \tag{3.1}
\]

The long-to-long part of `G_nest`, refined by source flag `alpha` and head
flag `beta`, has pair-count matrix

\[
\begin{pmatrix}
4827&4407&5770&14488\\
0&1196&2295&5668\\
0&0&1276&4528\\
0&0&0&4738
\end{pmatrix}.                                         \tag{3.2}
\]

The zero triangle is structural.

### Theorem 3.1 (upper-triangular flag drift)

Every legal long-to-long transition satisfies

\[
                              \alpha\leq\beta.          \tag{3.3}
\]

Therefore every state-consistent directed cycle containing only long rows
has constant flag, every all-long strongly connected component of the
**flag-state-expanded graph** lies in one diagonal flag layer, and flags are
nondecreasing along each maximal long block between short rows.

#### Proof

Suppose `alpha>beta`.  Equality of the two retained source cells forces

* `L_j=L_i` for flag pairs `(1,0),(2,0),(3,2)`; or
* `M_j=M_i` for flag pairs `(2,1),(3,0),(3,1)`.

The frozen table is a chain partition: every named lower target and every
named rank-seven target occurs in exactly one row.  Thus either equality
forces `j=i`.  But a self-transition cannot carry owner `T_i`: every cell
of a state for row `i` lies inside `U_i`, whereas the entering cell would
have to contain the nonempty increment `T_i-U_i`.  Hence no decreasing
flag arc exists, proving (3.3).

Following (3.3) around a directed cycle forces equality at every step.
The SCC and block statements follow.  \(\square\)

The diagonal of (3.2) contains `12,037` flag-labelled row--head incidences
(not necessarily `12,037` distinct raw projection edges), so the diagonal
layers alone cannot cover all `18,646` hard heads.  Short rows are the only
possible flag-reset sockets inside this one-transition model.  The complete
short-row union has already been included in Theorem 2.1 and is still
deficient; no positive regeneration theorem follows from this observation.

## 4. Consequences for rotor fusion

The conditional factor-critical hinge theorem remains correct, but this
fixed table cannot supply its bridge atlas solely with one-transition nested
addresses.  State synchronization, cycle consistency, connected Euler
topology and residence could only delete choices from `G_nest`; they cannot
repair Theorem 2.1.

Thus the smallest still-live fixed-table mechanisms are:

1. a nonnested or otherwise noncontiguous address for at least one named
   payload;
2. a genuinely multi-transition or multi-row bridge which realizes a hard
   payload without assigning it one predecessor arc in `G_nest`; or
3. a change of the static chain/owner assignment itself.

This is a finite K17 obstruction, not an all-`k` theorem.  It makes no claim
about residence histories, arbitrary-width upper shadows, source-word
factorability, a common cap, compiler Hall, or a final word.

## 5. Frozen artifacts and independent replay

The immutable local mirror is

```text
scratch/a_k17_four_flag_short_projection_20260802/
```

with hashes

```text
frozen source       b1dd4f4bb727e8c6afbb726e30fe58a1fe4aa5cbad3cffe79f56baf127558ff0
remote binary       5aa3f6885e9f63f809a841f0a5ae4c583a74394f133190d011623c836d01703d
static table        029d3be53e13186e7be4c5bd8b89de9d3610be05c3af15f8c9024e7fbf3396c1
matching witness    e864b22784904e5796e1f8ad26a6eb6e42dce2efe34a74f6896b2342bcc53ddf
run output          d8019ad0018198e9ee5f900478ef7f9b5bee756cf54a9fc6eb4aae3119f55616
run stderr          27e2ead4cbb597e287320d2d8c4241fc992e2db9d41a12c02686bf57554e6d81
remote manifest     478c3ac3ff74cd56d2c4aa1ff1f41251744e296e39f868813cabc909f44b9bf7
```

The separate long-only matrix audit used in (3.2) is

```text
source               d70ca3992137d2f1ffcc39a558877054bab5b587fe69da3568fe83b4eb1ccbd5
matrix output        c63de98bddcd749ef853e1f12d644f7bd8e6aa3efbd69d4d67ac952828156d7e
matching witness     190a5ca2f9f5dccf590196c42264d3edf18c2ea4e5f02b173ed9e73ead4cfaae
```

The independent lightweight replay has hashes

```text
verifier             b28547ae26c52d52e1bbc9547ceb75e2ab41fb93ddc502bb786512da0d218561
audit JSON           036b5afc09a59752678ad5c943cf7f42cb90893a3ca54d1836bed6ebe216b029
audit text           42ef7c3d48295d7e7c6cb876c3f5ed4f031b7229c661bec7f8ea9390c1e2cda2
```

It authenticates the frozen source, table, run output and witness; rebuilds
the `6/9/4` flag families; and independently replays all `18,162` selected
flag-pair masks.  It explicitly does not rebuild all `71,806` edges or
recompute Hopcroft--Karp optimality.
