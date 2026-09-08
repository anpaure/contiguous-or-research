# Six-way recency ports and the current k17 flat source bank

2026-09-08. Pure local proof and source reads. No mathematical program
was run, and no source word was changed.

The user's six-way move-to-front biclique is valid, as independently
proved in
RECENCY_BICLIQUE_AND_COHERENT_CLASS_FUSION_INDEPENDENT_AUDIT_20260908.md.
This note concerns its applicability to the actual 1513-stage bank.

**Conclusion:** the twelve proposed port states do not occur in the
unchanged bank. Preserving each good rank-seven pair union also forbids
creating them by capping. More strongly, keeping a flat schedule of
distinct rank-nine four-window owners forbids either port in its
protected interior, even when pair unions are allowed to change.
These are local interface obstructions, not a disproof of the recency
gadget, of a different state inventory, or of exact equality.

## 1. The actual source properties used

The current bank consists of 132 cyclic good sources, with 24,004 source
positions in total, plus the fixed 308-letter shallow source for the
306-owner prefix. The sources are recorded in

* K17_NINE_COMPONENT_1513_FUSION_AND_PARENT_FAMILY_SATURATION_20260908.md;
* K17_LOWER_BANK_FINAL_1513_INCREMENTAL_AUDIT_20260908.md; and
* K17_PBBS_ALLPORTS_JOHNSON_306_OWNER_PREFIX_20260908.md.

The independently checked literal facts are:

1. Every good source letter has rank six.
2. Every cyclic adjacent good pair has union of rank seven.
3. Every cyclic four-window is its prescribed rank-nine owner, and
   all these owners are distinct.
4. Every shallow-prefix letter has rank at least seven.
5. The 306 consecutive three-windows of the shallow source are its
   306 distinct prescribed rank-nine owners.

The good triple unions also have rank eight, although that extra fact
is unnecessary for the main obstruction.

## 2. What a recency prefix means in a literal word

For a finite history A_1,...,A_i, assign to every seen coordinate its
latest occurrence time. Group equal times, with newest time first.
If the resulting ordered partition is B_1|...|B_m, then the distinct
nonempty suffix unions ending at i are exactly

    B_1, B_1 union B_2, ..., B_1 union ... union B_m.     (1)

Indeed, extending a suffix backwards adds precisely the coordinates
whose most recent occurrence is newly crossed. Several consecutive
suffix lengths may give the same union, but every time-class prefix
in (1) occurs at its corresponding threshold. In particular B_1=A_i.
This is the already established move-to-front theorem, MASTER_HANDOFF
section 1.2; no new probabilistic interpretation is involved.

For a cyclic word, use the most recent occurrence in the preceding
period, on the active alphabet U=union A_i. These finite backward
distances define the canonical periodic recency state. Its prefix
unions are exactly the distinct cyclic suffix unions of lengths
1 through one period. Once an actual linear history has traversed
that period, the same state on U is obtained regardless of older
history on U.

Coordinates not yet seen cannot be silently supplied by a chosen
initial state. If a formal state retains older coordinates outside U,
its additional prefixes need not be literal intervals in the displayed
cycle. This issue does not weaken the obstruction below: the union
of the last two actual letters is always a recency prefix once both
letters have actually been read, even if still older coordinates
are present in the history.

## 3. The user's two port menus

Partition the 17 coordinates into H,C,D,G of sizes4,4,3,6. For Y a
two-subset of H and z in G, the proposed states are

    P_Y=(Y | C | D | H\Y | G),
    Q_z=(H union {z} | C | D | G\{z}).

Their prefix ranks are exactly

    P_Y: 2,6,9,11,17;
    Q_z: 5,9,12,17.                                    (2)

Appending H union {z} sends every P_Y to every Q_z. The six-by-six
biclique and its coherent rerouting theorem are preserved in the
separate proof note cited above.

No unchanged good endpoint has either state: its first recency block
has rank six, whereas (2) requires rank two or rank five. Likewise
the unchanged shallow prefix, whose letters have rank at least seven,
has neither state. This conclusion is independent of how the existing
cycles are rooted or what earlier history is supplied.

## 4. Pair preservation rules out cap-created ports

Let A'_j be any modified nonempty letters. At an endpoint i with an
actual preceding letter, suppose

    |A'_(i-1) union A'_i|=7.                            (3)

Equation (1) makes this pair union a prefix of the recency state at i.
Neither menu in (2) contains rank seven, so that state can be neither
P_Y nor Q_z.

In particular, any caps A'_j subseteq A_j preserving the named good
pair unions preserve (3) at every good cyclic endpoint. The statement
actually requires only preservation of their ranks, not their labels
or the cap relation. A counter-preserving modification also has the
same implication if it leaves every current good adjacent pair with
rank seven.

This does not say that the global rank-seven target support alone
forces (3) at the same positions. A surgery could move those witnesses
elsewhere and change the local pair ranks; that is outside this
particular obstruction.

## 5. A stronger local obstruction from flat owner uniqueness

Here is a general deterministic lemma.

Let q>=2. Suppose a nonempty set-word has consecutive q-window
unions

    W_j=A_j union ... union A_(j+q-1)

all of rank R, and adjacent owners are distinct. At an endpoint i,
assume precisely that W_j has rank R for i-q+1<=j<=i, and
W_j!=W_(j+1) for i-q+1<=j<=i-1.
Then the q successive suffix unions

    S_l=A_(i-l+1) union ... union A_i,   1<=l<=q,

are strictly increasing, and |S_q|=R.

Proof. If S_l=S_(l-1) for some2<=l<=q, put j=i-l+1. Then
A_j is contained in A_(j+1) union ... union A_i. Because i<=j+q-1,
A_j is also contained in the remaining q-1 letters of W_j. Hence

    W_j subseteq W_(j+1).

Both sets have rank R, so they are equal, contradicting the adjacent
owner hypothesis. Thus every addition is strict. The last union is
W_(i-q+1), of rank R. This proves the lemma.

Consequently, the recency state at such an endpoint has at least q-1
distinct prefix unions below rank R. Equivalently, its unique prefix
of rank R occurs no earlier than its qth block.

For the current good source q=4 and R=9. A protected recency state
must have at least three prefix ranks below nine. P has only two,
and Q only one. Thus neither state can occur under ANY modification
preserving the flat, distinct rank-nine four-window schedule in that
neighborhood. This conclusion does not require pair preservation,
letter rank six, or a monotone cap relation.

In particular, arbitrary capping that preserves all the present cyclic
four-window owners cannot create these ports. Allowing the lower pair
unions to shrink does not evade this stronger frozen-schedule test.
Even a different owner ordering cannot evade it if the resulting
word still has distinct rank-nine four-windows everywhere.

For the shallow source q=3 and R=9, the same lemma excludes Q at
protected interior endpoints. P is not excluded by this count alone:
it has two prefix ranks below nine. Realizing it would still require
changing its current letter and lower-target witnesses. No such cap
or realization is constructed here.

This lemma is a local application of equal-rank owner uniqueness.
It is not the false assertion that an optimal word must have a flat
middle row. Variable witness lengths are explicitly outside its scope.

## 6. Cuts, starts, and the exact remaining possibility

For a cyclic good source the hypotheses in section 5 hold at every
endpoint, including across its existing closure. Merely rotating the
cycle does not remove the obstruction.

If a cyclic source A_1,...,A_N is cut open and only its internal
four-windows are kept, the sufficient local condition of section 5
holds at endpoints4<=i<=N-3: it needs the four-windows ending at
i,i+1,i+2,i+3. The first and last three endpoints can lose one or more
of these protected constraints. A collar restoring the missing
windows also restores the corresponding obstruction.

For caps preserving every internal rank-seven pair, section 4 is
stronger near the ends: it still excludes both states at every
endpoint2<=i<=N. Only the first endpoint lacks its old incoming-pair
constraint. If the word really starts from the empty history, that
endpoint has the single-block state A'_1, not a full five- or four-block
port. If the cut is attached to another nonempty history, its new
incoming pair must instead be audited; the old cyclic constraint need
not survive.

There is an analogous q-1 endpoint collar qualification for the shallow
three-window prefix. In a completely new source with altered witness
lengths, lower rows, or boundary schedules, the menus in (2) might be
realizable. The present result does not exclude that possibility.

Thus the accepted six-way theorem is a real algebraic construction
tool, but it does not yet supply a zero-cost splice of the current
132-cycle/1513-stage bank. An application must first construct the
required ports, protect or replace the affected named target witnesses,
and verify actual initialization. Those concrete interfaces remain
open; no new bound on nu(17) or proof of nu(k)=B(k) is claimed.
